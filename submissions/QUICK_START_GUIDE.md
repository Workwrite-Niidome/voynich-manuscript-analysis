# 最速で世界に公開する手順（15分）

このガイドは、ヴォイニッチ手稿の分析論文を最速で世界に公開するためのステップバイステップ手順です。各ステップでコピペする内容は別ファイルに用意済みです。

---

## Step 1: arXivに投稿（最も重要・最優先）

arXivに論文を公開することで、永続的なURLが得られ、他の全ての投稿でリンクできるようになります。

### 1-1. 匿名メールアドレスの作成（5分）

1. https://proton.me にアクセス
2. 「Create a free account」をクリック
3. ユーザー名を決める（例: `voynich.analysis.2026@proton.me`）
4. パスワードを設定
5. アカウント作成完了 -- このメールアドレスをarXivとRedditで使う

### 1-2. arXivアカウント作成（5分）

1. https://arxiv.org/user/register にアクセス
2. 以下を入力:
   - **Email**: 上で作成したProtonMailアドレス
   - **Username**: 任意（例: `voynich_analysis`）
   - **Name**: 論文の著者名（ペンネーム可）
3. 確認メールが届くのでリンクをクリック
4. アカウント有効化まで **1--3営業日** かかる場合あり

### 1-3. 論文の準備

arXivはLaTeX形式を推奨。最低限、以下の手順で変換:

```bash
# pandocがインストール済みの場合
pandoc FINAL_PAPER_v3.md -o voynich_analysis.tex --standalone

# PDFに変換（メール添付用にも使える）
pandoc FINAL_PAPER_v3.md -o voynich_analysis.pdf --pdf-engine=xelatex
```

pandocが未インストールの場合: https://pandoc.org/installing.html からインストール

代替手段: Markdown形式のままPDF化して投稿することも可能（arXivはPDFも受け付ける）

### 1-4. arXivに投稿（5分）

1. https://arxiv.org/submit にアクセス（ログイン済みであること）
2. 「Start New Submission」をクリック
3. 各フィールドに入力する内容は **`ARXIV_METADATA.txt`** にコピペ用で用意済み:
   - **Title**: そのままコピペ
   - **Authors**: そのままコピペ
   - **Abstract**: そのままコピペ
   - **Primary Category**: `cs.CL (Computation and Language)` を選択
   - **Cross-list Categories**: `cs.AI`, `cs.DL` を追加選択
   - **Comments**: そのままコピペ
   - **License**: `CC BY 4.0` を選択
4. ファイルをアップロード（.tex または .pdf）
5. 「Submit」をクリック

### 1-5. Endorsement（推薦）について

- **cs.CL** カテゴリは初回投稿者にendorsementを求める場合がある
- 求められた場合の対処法:
  1. まず **cs.DL (Digital Libraries)** で投稿を試す（endorsement不要の場合が多い）
  2. それでもダメなら `arxiv-moderation@cornell.edu` に状況を説明するメールを送る
  3. cs.CLに過去に投稿した知人がいれば、endorseを依頼する

### 1-6. 補足データのホスティング

273ファイルのアーカイブはarXivの50MB制限を超える可能性があるため:

1. https://zenodo.org にアクセス（無料、DOI付与、永続保存）
2. GitHubアカウントでログイン可能
3. 「New Upload」でアーカイブをアップロード
4. 取得したDOI/URLを論文の「Data Availability」セクションに追記

---

## Step 2: Redditに投稿（即座・arXiv公開後）

arXivのURLが確定したら即座に投稿可能。

### 2-1. Redditアカウント作成

1. https://www.reddit.com/register にアクセス
2. 匿名ユーザー名で作成（ProtonMailアドレスを使用）

### 2-2. r/voynich に投稿

1. https://www.reddit.com/r/voynich/ にアクセス
2. 「Create Post」をクリック
3. 「Text」タブを選択
4. **`REDDIT_READY.txt`** の内容をそのままコピペ:
   - Title行 → タイトル欄にコピペ
   - Body → 本文欄にコピペ
5. `[arXiv:XXXX.XXXXX]` を実際のarXiv URLに置換
6. 投稿

### 2-3. r/cryptography にクロスポスト

1. https://www.reddit.com/r/cryptography/ にアクセス
2. r/voynichの投稿から「Share」→「Crosspost」を選択
3. または `REDDIT_READY.txt` の内容で新規投稿

### 2-4. 追加のサブレディット（任意）

- **r/linguistics** -- 形態素解析の知見を強調
- **r/ArtificialIntelligence** -- AI手法の角度で
- **r/history** -- 歴史的文脈で

### 2-5. 投稿タイミングのコツ

- 米国時間の平日午前中（日本時間の火--木の深夜0時--午前3時頃）が最もリーチが大きい
- 投稿後2--3時間はコメントに返信する

---

## Step 3: 研究者にメール送信（arXiv公開後）

### 3-1. 準備

- arXivのURLが確定していること
- **`EMAIL_READY.txt`** に4人分のメール本文がコピペ用で用意済み

### 3-2. 送信手順

1. メールアプリを開く（ProtonMailまたは通常のメール）
2. `EMAIL_READY.txt` から各研究者のTO / SUBJECT / BODY をコピペ
3. `[arXiv:XXXX.XXXXX]` を実際のarXiv URLに置換
4. `[Name]` と `[Contact email]` を自分の情報に置換
5. 個別に送信（一斉送信しない）

### 3-3. 研究者の連絡先の見つけ方

| 研究者 | 探し方 |
|--------|--------|
| Lisa Fagin Davis | Medieval Academy of America の公式サイトで検索 |
| Rene Zandbergen | voynich.nu のコンタクトページ |
| Nick Pelling | ciphermysteries.com のコンタクトフォーム |
| Michael Greshko | Google Scholar等で所属機関を確認 |

### 3-4. 送信タイミング

- arXiv公開の1--2日後
- 火曜--木曜に送信
- 各メールは数時間あけて送信（スパム扱い回避）

---

## Step 4: Wikipedia（arXiv公開後・急がない）

Wikipediaへの追記は最も慎重に行うべきステップです。

### 4-1. 前提条件

- arXivプレプリントが公開済み
- できればメディア報道や学術的な言及があること（二次ソースが理想）

### 4-2. 手順

1. https://en.wikipedia.org/wiki/Special:CreateAccount でアカウント作成
2. まず他の記事で数件の小さな編集をする（善意の編集者として実績を作る）
3. https://en.wikipedia.org/wiki/Talk:Voynich_manuscript にアクセス
4. 「New section」をクリック
5. 以下のような提案を投稿:

```
== Proposal: Addition of 2026 AI structural analysis ==

A recent computational analysis (arXiv:XXXX.XXXXX) presents validated 
structural findings including cross-word suffix dependencies and blind 
prediction testing. The paper reports both confirmed and refuted hypotheses. 
I believe this may be relevant to the "Analysis" or "Theories" section.

I am disclosing that I am connected to this research (per WP:COI). 
I am proposing this edit rather than making it directly, in line with 
Wikipedia policy. I welcome the community's judgment on whether this 
merits inclusion.

Sources:
* [arXiv link]
* [any media coverage links]
```

6. 他の編集者の判断を待つ（自分で直接記事を編集しない）

### 4-3. 重要なWikipediaポリシー

- **WP:COI**: 自分の研究は直接追記せず、Talk pageで提案する
- **WP:RSPRIMARY**: arXivプレプリントは一次ソース。二次ソース（報道等）があると通りやすい
- **WP:WEIGHT**: 追記は研究の重要性に比例したサイズにする

---

## ファイル一覧

| ファイル | 用途 |
|---------|------|
| `ARXIV_METADATA.txt` | arXiv投稿フォームの各フィールドにコピペ |
| `REDDIT_READY.txt` | Reddit投稿のタイトルと本文をそのままコピペ |
| `EMAIL_READY.txt` | 各研究者へのメール（TO/SUBJECT/BODY）をそのままコピペ |
| `FINAL_PAPER_v3.md` | 論文本体 |
| `ARXIV_PREPRINT.md` | arXiv投稿の詳細ガイド |

---

## 全体タイムライン

| 日 | アクション |
|----|-----------|
| Day 1 | ProtonMailアカウント作成、arXivアカウント作成 |
| Day 1 | 論文をLaTeX/PDFに変換、Zenodoにアーカイブアップロード |
| Day 2-3 | arXivアカウント有効化を待つ |
| Day 3 | arXivに論文を投稿 |
| Day 4-6 | arXivプレプリント公開（モデレーション通過後） |
| Day 5-7 | Redditに投稿、研究者にメール送信 |
| Day 30+ | Wikipediaに提案（二次ソースが出た後） |
