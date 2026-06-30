# Contributing to FTShare Skills

感谢你关注 `FTShare-skills`。

本仓库是 ftshare 生态的 Agent Skill 大仓库，用于沉淀金融数据 Skill 和投研业务 Skill。贡献内容主要分为两类：

1. 数据级 Skill：封装 FTShare 金融数据接口，让 Agent 能稳定获取结构化数据。
2. 业务级 Skill：围绕个股分析、财报解读、行业分析、复盘、持仓分析等投研任务组织工作流。

## 开发准备

克隆仓库：

```bash
git clone git@github.com:ftshare-lab/FTShare-skills.git
cd FTShare-skills
```

查看当前可用 Skill：

```bash
python FTShare-market-data/run.py
```

## 新增或修改 Skill

提交新 Skill 或修改现有 Skill 时，请保持：

- 每个 Skill 有独立 `SKILL.md`
- 每个 Skill 包有自己的 `README.md`
- 参数命名清晰
- 示例命令可执行
- 输出结构稳定，优先使用 JSON
- 下载类接口限制输出路径
- README 与实际能力保持同步
- 数据级 Skill 与业务级 Skill 职责清晰分离

## 业务级 Skill 要求

新增业务级 Skill 时，建议至少说明：

- 适用场景
- 输入参数
- 调用的数据能力
- 输出结构
- 示例问题
- 示例结果
- 数据质量与风险提示

## 提交流程

1. 从 `main` 拉取最新代码。
2. 新建功能分支。
3. 完成 Skill、文档和示例。
4. 本地运行相关命令，确认输出正常。
5. 提交 Pull Request，并说明修改内容和使用场景。

## 问题反馈

普通问题、功能建议和文档改进可以通过 GitHub Issue 或 Pull Request 提交。

安全相关问题请不要公开提交 Issue，请参考 [SECURITY.md](SECURITY.md)。
