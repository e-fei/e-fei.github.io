# 内容填写示例

下列均为字段说明，不会发布到主页。把 `_data/homepage.yml` 对应的空数组替换为自己的条目。

```yaml
intro: "在这里填写个人简介，可以使用 Markdown 链接。"
research_interests:
  - "研究方向一"
news:
  - date: "2026.09"
    text: "真实的学术动态"
experience:
  - institution: "学校或机构"
    date: "2024 – Present"
    role: "专业、学位或职位"
    description: "研究内容或导师信息"
    # logo: "/images/institution.png"
publications:
  - title: "真实论文标题"
    authors: "完整作者列表"
    venue: "会议 / 期刊，年份"
    description: "一句话介绍论文贡献"
    selected: true
    # image: "/images/paper.png"
    # paper: "真实论文链接"
    # code: "真实代码仓库链接"
projects:
  - title: "项目标题"
    description: "项目描述"
    # url: "真实项目链接"
awards: []
services: []
talks: []
cv: "" # 上传 PDF 后填写 /files/cv.pdf
```

未提供的链接留空，不要填示例地址。日期请加引号。照片上传到 images 后，在 `_config.yml` 的 author.avatar 中填写文件名。
