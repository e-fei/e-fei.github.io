# 陆逸霏（Yifei Lu）的学术主页

基于 [WowPage](https://github.com/oplisty/oplisty.github.io)，保留原模板侧栏、顶部导航、玫瑰色点缀和卡片布局。

主页地址：https://e-fei.github.io/

## 修改资料

- `_config.yml`：姓名、机构、邮箱、头像、Google Scholar 等。
- `_data/homepage.yml`：简介、研究兴趣、新闻、经历、论文、项目、奖项等。
- `images/`：头像、论文配图、学校标志。
- `_data/navigation.yml`：顶部导航。
- `assets/css/home.css`：主页样式。

当前已填写姓名、学校、视频生成研究方向、上海交通大学研究经历及三项竞赛获奖，并允许搜索引擎收录。
未填写的新闻、论文和项目栏目自动隐藏；在 `_data/homepage.yml` 添加内容后会自动显示。
头像目前使用姓名首字母，可在提供个人照片后替换。保留原模板署名，不包含模板原作者的个人经历、照片、论文或联系方式。

## 部署到 GitHub Pages

仓库名称：`e-fei.github.io`。在 Settings → Pages 中选择 Deploy from a branch，使用 `main` 分支的 `/ (root)` 目录。GitHub Pages 会使用 Jekyll 自动构建，之后每次推送都会更新网站。

本地预览：`bundle install`，然后 `bundle exec jekyll serve`。

内容填写示例见 [CONTENT_GUIDE.md](CONTENT_GUIDE.md)。

## 模板来源与许可

改编自 oplisty/oplisty.github.io 的 WowPage，源自 Academic Pages。
保留原 MIT 许可证及 Yue Su、Weidong Tang 的版权声明，见 LICENSE。
