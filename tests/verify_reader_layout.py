"""Regression checks for index2.html sidebar layout in offline file:// mode.

Run: python tests/verify_reader_layout.py
Requires Playwright and its Chromium browser (python -m playwright install chromium).
Optional screenshots: --screenshots <directory>
"""
from argparse import ArgumentParser
from pathlib import Path
import json
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
READER = ROOT / '온톨로지 따라하기' / 'index2.html'


def check_layout(page, opened):
    expect(page.locator('#sidebar-toggle')).to_have_attribute('aria-expanded', str(opened).lower())
    if opened:
        expect(page.locator('#sidebar')).to_be_visible()
    else:
        expect(page.locator('#sidebar')).to_be_hidden()
    geometry = page.evaluate('''() => {
        const box = selector => {const r=document.querySelector(selector).getBoundingClientRect();return {x:r.x,width:r.width,right:r.right};};
        return {shell:box('.shell'),workspace:box('#workspace'),frame:box('#reader'),pane:box('.reader-pane'),sidebar:box('#sidebar'),mobile:matchMedia('(max-width:760px)').matches,viewport:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth};
    }''')
    main = geometry['workspace']
    shell = geometry['shell']
    assert not geometry['overflow'], geometry
    if not opened or geometry['mobile']:
        assert abs(main['x']-shell['x']) <= 1, geometry
        assert abs(main['width']-shell['width']) <= 1, (
            'Hidden sidebar must leave a full-width reading pane', geometry
        )
    else:
        assert abs(main['x']-geometry['sidebar']['right']) <= 1, geometry
        assert abs(main['right']-shell['right']) <= 1, geometry
    assert geometry['frame']['width'] > 300, geometry
    assert abs(geometry['frame']['width']-geometry['pane']['width']) <= 1, geometry
    return geometry


def main():
    parser = ArgumentParser()
    parser.add_argument('--screenshots', type=Path)
    args = parser.parse_args()
    if args.screenshots:
        args.screenshots.mkdir(parents=True, exist_ok=True)
    results=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        try:
            for width,height in [(1440,1000),(1920,1080),(761,900),(760,900),(390,844)]:
                context=browser.new_context(viewport={'width':width,'height':height})
                context.set_offline(True)
                page=context.new_page()
                errors=[]
                page.on('pageerror',lambda error:errors.append(str(error)))
                page.goto(READER.as_uri()+'#page=426525')
                expect(page.frame_locator('#reader').locator('h1')).to_contain_text('Apache AGE')
                original_title=page.locator('#reader-title').inner_text()
                opened=width>760
                check_layout(page,opened)
                for _ in range(3):
                    page.locator('#sidebar-toggle').click()
                    opened=not opened
                    geometry=check_layout(page,opened)
                    expect(page.locator('#reader-title')).to_have_text(original_title)
                    expect(page.frame_locator('#reader').locator('h1')).to_contain_text('Apache AGE')
                    page.locator('#sidebar-toggle').click()
                    opened=not opened
                    check_layout(page,opened)
                if opened:
                    page.locator('#sidebar-toggle').click()
                geometry=check_layout(page,False)
                if args.screenshots and width in (1440,390):
                    page.screenshot(path=str(args.screenshots/f'collapsed-{width}.png'))
                page.reload()
                check_layout(page,False)
                expect(page.frame_locator('#reader').locator('h1')).to_contain_text('Apache AGE')
                page.locator('#sidebar-toggle').click()
                check_layout(page,True)
                if args.screenshots and width==1440:
                    page.screenshot(path=str(args.screenshots/'expanded-1440.png'))
                assert not errors, errors
                results.append({'viewport':width,'collapsed_main_width':geometry['workspace']['width'],'toggle_roundtrips':3,'reload_hidden':'passed','content_preserved':True,'javascript_errors':errors})
                context.close()
        finally:
            browser.close()
    print(json.dumps({'passed':True,'cases':results},ensure_ascii=False))


if __name__=='__main__':
    main()
