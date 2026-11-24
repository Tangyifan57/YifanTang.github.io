# Yifan Tang · 唐逸钒

Personal academic website built with Jekyll and hosted on GitHub Pages.

## 在线编辑

无需安装软件。打开对应文件，点击铅笔 **Edit this file**，修改后点击 **Commit changes**。

| 要更新的内容 | 文件 |
| --- | --- |
| 姓名、邮箱、Scholar 链接、导航、网址 | `_config.yml` |
| 首页个人介绍、研究兴趣、联系方式 | `index.md` |
| 论文、作者、DOI、发表状态 | `_data/publications.yml` |
| 教育背景、导师 | `_data/education.yml` |
| 动态 | `_data/news.yml` |
| 研究内容 | `research.md` |
| 网页版 CV | `cv.md` |
| 下载版 CV | `assets/files/Yifan_Tang_CV.pdf` |
| 头像 | `images/yifan-portrait.webp`（可在 `_config.yml` 修改 avatar） |
| 生活照片与图注 | `_data/life.yml`、`images/life/` |
| 学校校标 | `_data/education.yml`、`images/schools/` |
| 论文 TOC | `_data/publications.yml`、`images/papers/` |
| 个人样式 | `assets/css/yifan.css` |

详细操作与新增论文示例请看 [EDITING_GUIDE.md](EDITING_GUIDE.md)。

## GitHub Pages 首次上线

当前仓库为项目站点，默认地址：`https://tangyifan57.github.io/YifanTang.github.io/`。

打开仓库 **Settings → Pages → Build and deployment**：

1. Source 选择 **Deploy from a branch**。
2. Branch 选择 **main**，目录选择 **/(root)**。
3. 点击 **Save**，在 **Actions** 查看构建结果，等候页面提供正式访问链接。

后续提交 Markdown/YAML 修改后，GitHub Pages 自动重新构建。

若将仓库改名为 `Tangyifan57.github.io`，请同时把 `_config.yml` 中 `baseurl` 改为 `""`；不要只改仓库名。

## 本地预览（可选）

安装 Ruby 和 Bundler 后：

```bash
bundle install
bundle exec jekyll serve
```

访问终端提示的网址（保留 `/YifanTang.github.io/` 路径）。

## 内容说明

内容依据 2026-11-24 提供的 CV 整理。在审稿件单列；不展示影响因子或未经核实的指标。公开 PDF 仅保留专业联系邮箱和城市，未包含个人手机号及详细地址。

保留 MIT 模板许可，见 [LICENSE](LICENSE) 与 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
