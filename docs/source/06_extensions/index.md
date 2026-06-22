# 第6章：拡張機能の開発

## 学習目標

- Sphinx 標準拡張と主要なサードパーティ拡張を知る
- **カスタムディレクティブ**を作成する（HTML + LaTeX 両対応）
- **カスタムインラインロール**を作成する

```{toctree}
:maxdepth: 2

builtin
third-party
custom-directive
custom-role
```

## この章で実装するカスタム拡張

Sphinx マスタークラスでは 3 つのカスタム拡張を `_ext/` ディレクトリに実装しています。

| ファイル | 提供する機能 | 例 |
|---|---|---|
| `card_directive.py` | `{card}` ディレクティブ | カードブロックを描画 |
| `badge_role.py` | `{badge-*}` インラインロール | バッジラベル |
| `step_counter.py` | `{step}` ディレクティブ | 自動番号ステップ |

これらの拡張はこの文書全体で使用されています。使用例:

```{card} カードの例
:icon: 📊

このカードは `card_directive.py` カスタム拡張で描画されています。実装詳細は {doc}`custom-directive` で学びます。
```

{badge-new}`New` {badge-tip}`実践的` {badge-warn}`要注意`
↑上記は `badge_role.py` カスタムロールで描画されています。
