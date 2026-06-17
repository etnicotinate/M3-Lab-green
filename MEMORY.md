# 记录

- 当前项目是基于 Lab Website Template 的 Jekyll 静态网站，导航由带 `nav` front matter 的 Markdown 页面自动生成。
- 用户偏好保持现有目录结构，页面内容优先用 Markdown 和 Liquid includes 实现。
- `contact` 页面已迁移到 `joinUs/index.md`，网站导航应以 `JoinUs` 呈现；团队页加入按钮链接应指向 `joinUs`。
- `joinUs/comput-resources.csv` 记录组内计算资源，可在 JoinUs 页面展示为 Markdown 表格。
- `404.html` 是独立 Canvas 砖块小游戏页面，不走 Jekyll layout；已加入开始、暂停、初速设置和 5x7 点阵文字布局。
- 用户明确说明现有中文字符有用，先保留；仅按需求局部调整英文展示，后续再考虑中文国际化接口。
- Header 右上方导航已加入固定 `Home` 链接，位置在自动生成的页面导航之前。
- Research 页面 citations 后处理由 `_cite/mark_authors.py` 负责：从 `_members` 生成 `_data/group_members.yaml`，并给 citations 中的组内成员作者自动补 `#`；脚本会从文件名派生姓名别名以减少中英文姓名顺序漏标；`*` 和 `†` 仍需在源数据中显式维护。
- 组内成员作者标记必须同时加 `#` 和加粗，目标格式为 `**Name#**`，由 citation 组件的 `markdownify` 渲染。
- Research 搜索已优化：citation 组件预生成 `data-search`，`_scripts/search.js` 用 `WeakMap` 缓存搜索文本，减少每次输入时的 DOM 文本扫描。
- 正文字号暂未定位到正确控制点；已确认 `_styles/body.scss`、`_styles/paragraph.scss` 的 `p`、`_styles/feature.scss` 的 `.feature-text` 都不是合适修改点，后续需通过浏览器 DevTools 或构建 CSS 定位真实生效规则。
- 参考 Lab Website Template 和 Jekyll 文档后，正文字号采用 `_styles/z-text.scss` 作为末尾覆盖样式；该文件只覆盖 `main` 内文本选择器，避免改动 feature 布局或图片尺寸。修改 `_styles/*.scss` 后必须 rebuild/serve 才会更新 `_site` 中的 CSS。
- `News` 和 `Projects` 页面暂时保留文件但移除 `nav`，不显示在 header 导航中；后续完善后可恢复 `nav` 配置。
- 本项目本地测试方法：用 Git Bash 运行 `.docker/run.sh`，Docker 容器会挂载当前项目并暴露 `http://localhost:4000`，可在容器内测试 Jekyll 构建和页面效果。
- 正文字号覆盖值为 `_styles/z-text.scss` 中桌面端 `1.12rem`、移动端 `1.06rem`；此前 `1.06rem/1.03rem` 视觉变化过弱。
