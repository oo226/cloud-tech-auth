import os

platforms = [
    ("douyin", "抖音极速版"),
    ("kuaishou", "快手极速版"),
    ("xigua", "西瓜视频"),
    ("toutiao", "今日头条极速版"),
    ("hema", "河马剧场"),
    ("hongguo", "红果短剧"),
    ("alipay", "支付宝视频号"),
]

html_success = """<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><title>授权成功</title>
<style>
  body{{ font-family: "Microsoft YaHei"; text-align: center; padding: 60px; background: #f0f8ff; }}
  .msg {{ font-size: 24px; margin: 16px; color: green; }}
</style></head><body>
  <div class="msg">云朵科技接口 ✅ {plat_name}账号授权成功</div>
  <div class="msg">✅ 平台账号已关联成功</div>
  <div class="msg">✨ 今日金币增长中...</div>
</body></html>
"""

html_fail = """<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><title>授权失败</title>
<style>
  body{{ font-family: "Microsoft YaHei"; text-align: center; padding: 60px; background: #fff5f5; }}
  .msg {{ font-size: 24px; margin: 16px; color: red; }}
</style></head><body>
  <div class="msg">云朵科技接口 ❌ 授权失败</div>
  <div class="msg">平台账号关联失败，请换账号重试</div>
</body></html>
"""

os.makedirs("docs", exist_ok=True)
for code, plat in platforms:
    with open(f"docs/{code}-success.html", "w", encoding="utf-8") as f:
        f.write(html_success.format(plat_name=plat))
    with open(f"docs/{code}-fail.html", "w", encoding="utf-8") as f:
        f.write(html_fail)
print("已生成 docs/ 下 14 个 HTML 页面。")
print("下一步：提交到 GitHub 仓库并启用 Pages，即可获取永久链接。")