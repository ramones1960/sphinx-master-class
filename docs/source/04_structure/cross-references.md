# 相互参照

Sphinx の相互参照は、ファイルパスではなく **ID（ラベル）** で参照するため、
**リンク先を移動・改名しても壊れにくい**という特徴があります。

## ページ全体への参照（`{doc}`）

```markdown
{doc}`見出しテキスト <ファイル名>`

# 例
{doc}`開発ガイド <../01_introduction/install-local>`
{doc}`install-local`   # 見出しを自動使用
```

## 見出しへの参照（`{ref}`）

### ラベルを付ける

```markdown
(my-section-label)=
## この見出しにラベルが付く
```

### ラベルを参照する

```markdown
{ref}`セクション名 <my-section-label>`
```

### ラベルの命名規則

```
(<モジュール名>-<ベース名>-<説明>)=

# 例
(ch01-install-local-step1)=
(api-ref-endpoints-create)=
```

文書全体でラベルは**グローバルに一意**である必要があります。
命名規則を遵守することで重複を防ぎます。

## `{doc}` vs `{ref}` の選び方

| 用途 | 推奨ロール |
|---|---|
| ページ全体へのリンク | `{doc}` |
| ページ内の特定見出しへのリンク | `{ref}` |
| 外部 URL | `[text](https://...)` |

## 壊れた参照の検出

存在しないページ・ラベルを参照すると:

```
WARNING: undefined label: 'nonexistent-label'
WARNING: unknown document: 'nonexistent-page'
```

ビルド時に警告が出るため、リンク切れを早期に検出できます。
`-W` オプションを入れると警告をエラー扱いにできます（CI で役立つ）。

```bash
sphinx-build -W -b html docs/source docs/build/html
```

## 演習

:::{exercise} 演習 4-2: ラベルと相互参照を実践する

1. `docs/source/03_syntax/myst-markdown.md` の任意の見出しに `(myst-label)=` でラベルを付ける
2. 別のページから `{ref}` でその見出しを参照する
3. `{doc}` で存在しないページを参照して警告が出ることを確認する
:::
