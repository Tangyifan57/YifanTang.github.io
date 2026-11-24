# 网站编辑指南

## 直接在 GitHub 修改

打开仓库的 Code 页面，点击文件，再点击铅笔。修改后点击 Commit changes，选择提交到 main。GitHub Pages 会自动重新构建，通常需要几分钟。发现问题可在该文件 History 中恢复旧版本。

## 更新论文

打开 `_data/publications.yml`，复制一篇的结构。例如：

```yaml
- id: unique-paper-id
  title: "Your full paper title"
  authors: "Y. Tang#, A. Author#, B. Author*"
  journal: "Journal name"
  year: 2027
  volume: "12"
  article: "e12345"
  doi: "10.xxxx/example"
  role: "First author"
  selected: true
  material: "Material name"
  topic: "Short research topic"
  status: published
```

`selected: true` 让该论文出现在首页精选区；所有 `published` 条目都会出现在 Publications 页面。`status: under-review` 只出现在在审稿件区，不会混入已发表文章。DOI 只填编号，不要加 https://doi.org/。不要为在审稿件编造 DOI。

需要论文图片时，先上传到 `images/papers/`，再添加 `image: /images/papers/your-paper.jpg`。没有图片时显示材料名称和主题，不会显示假的论文图。

YAML 使用空格缩进，不要使用 Tab。包含冒号的文字用英文双引号包起来。姓名用 `Y. Tang` 时网页会自动加粗。

## 更换头像和图片

头像在 `images/yifan-portrait.webp`，也可以上传 JPG/PNG 后修改 `_config.yml` 中的 `owner.avatar`。首页、页头和手机联系菜单会共用这个配置。

生活照在 `images/life/`，页面文字与图片顺序在 `_data/life.yml`；导航中的 BEYOND RESEARCH 打开独立的生活照片页。

三个学校校标在 `images/schools/`，在 `_data/education.yml` 的 `logo` 字段中对应学校。

三篇论文 TOC 在 `images/papers/`，通过 `_data/publications.yml` 中的 `image` 字段关联论文。TOC 保持完整显示，点击可查看原尺寸。

首页介绍文字在 `index.md` 的 `about-intro` 区域中编辑；该区域正文使用常规字重并两端对齐。不要删除外层 `<section>` 标记。

## 更新工作经历与研究方向

工作经历在 `_data/experience.yml`，包括公司名称、任职时间、岗位、公司简介和个人职责。公司标志在 `images/companies/`，通过 `logo` 字段关联。`overview_source` 保存公司公开介绍的来源；个人职责以你提供的经历为准。

首页的三点研究兴趣在 `index.md` 的 `research-interests` 区域。研究页详细内容在 `research.md` 的 `research-content` 区域，正文为常规字重、两端对齐，行距为 1.65；小标题仍保留标题样式。

## 更新 CV

首页的 View CV 链接跳转到 `cv.md` 对应的 `/cv/` 页面，Download CV (PDF) 入口放在 CV 页面。下载 PDF 在 `assets/files/Yifan_Tang_CV.pdf`；上传新版同名 PDF 即可替换，或安装 Python 的 reportlab、PyYAML 后运行 `python3 scripts/build_cv.py`，依据网站教育、工作经历和论文数据重新生成。网页 CV 和 PDF 的研究经历等正文需要分别维护。上传前检查手机号和详细地址是否希望公开。

Research 不出现在顶部导航中；从首页 Research Interests 下方的 Read more about my research 链接进入。该页面仍保留 `/research/` 原网址。

## 更新动态

编辑 `_data/news.yml`，按从新到旧排列：

```yaml
- date: "Jan. 2027"
  text: "Your update in English."
```

## 修改网址

`url` 只放域名，`baseurl` 放项目路径。当前为：

```yaml
url: "https://tangyifan57.github.io"
baseurl: "/YifanTang.github.io"
```

内部图片、导航和文件通过 `relative_url` 自动带项目路径；不要将它们写成不带 baseurl 的 `/images/...` 链接。不要修改模板中已有的 Liquid 标记（`{{ ... }}` 和 `{% ... %}`）。

## 排查

Settings → Pages 查看部署来源；Actions 查看 pages build and deployment。构建失败时先检查 YAML 缩进、引号和 Markdown 顶部的 `---`。若页面仍旧，等待构建完成后再刷新。所有历史版本保存在 GitHub 提交记录中。
