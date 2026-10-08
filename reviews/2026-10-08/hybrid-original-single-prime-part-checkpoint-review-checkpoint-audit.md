# 480 精确子族成本与完整矩传递检查器：独立代码全文审查

2026-10-08。审查人：checkpoint_audit。结论：**限定 PASS**。

已全文实读最终Python检查器180行，独立核查冻结依赖、review绑定、链接结构、
Fraction成本与affine delta分支及--check只读控制流。
只保存本审查文件；本阶段没有执行build/main生成，没有写或替换任何检查点、旧文件或Git。
后续由root首次生成输出，再运行独立--check；本文件不预先声称该真实运行已完成。

## 1. 最终绑定和数学审查分工

canonical UTF-8 LF仅统一CRLF与孤立CR，不trim、不改变EOF。

| 绑定对象 | canonical LF SHA256 | 字节 / 行 |
|---|---|---:|
| [最终检查器](../../scripts/hybrid_original_single_prime_part_checkpoint.py) | af1014604fe3b3a02c74793ac4925f4bfdba46c9519c3e65f56d7f617e4d0bf4 | 10347 / 180 |
| [最终480数学文本](../../notes/480-original-type-ii-single-prime-part-and-whole-moment-transfer.md) | 13a6cbd697ad960cdb97543090861373f21b6970710bc2d247edac59bb08e791 | 7993 / 185 |
| [480独立数学全文审查](hybrid-original-single-prime-part-note-review-checkpoint-audit.md) | a5c2ec4542667e6d7f2b3a2f82aa78768aca49341250874a2d6c96d053c3d3d8 | 8409 / 146 |
| [完整子族研究源](hybrid-original-type-ii-small-single-prime-part-fourth-research-radial.md) | f0b740a85b09f70b68653bf3ec06288150876f1f761920ffb1107620fbf44580 | 11658 / 329 |
| [源的前轮全文独审](hybrid-original-type-ii-small-single-prime-part-fourth-review-checkpoint-audit.md) | 2066698dfe4079c6a174369cd48e05986d52a14177466f7b38b25fad4c2adb2f | 8197 / 151 |

本文件审的是程序实际能验证的有限有理式、最终哈希、存在性、链接和语义输出比较。
自然子族均值、全部移动端点、任意固定epsilon、完整norm前件及Hölder转移，
由上表不同作者数学审查分别核准。不能把本代码PASS当作无限解析认证。

## 2. 冻结依赖与真实检查范围

检查器先验证[已发表479检查点](../../output/hybrid-original-type-ii-factor-checkpoint.json)
的canonical SHA256为88ff98918fa6fda62996e848e120a7ffdf0030472b9709c94cb9f61ac5f09b1e，
然后读其中27个file snapshots。这阻止悄悄换用另一组旧依赖。
本轮另用独立只读程序逐文件重算，确认该27项全部保持原canonical SHA256。
这是重新核hash，不是重新运行其旧大核或七点覆盖。

FROZEN的9个直接绑定均已独立实核一致，包括480、完整子族源及旧独审、
476、Ivic完整研究源、root完整审查、positive-height零点包及fixed-start采样。
未从“PASS”字符串或hash存在直接推断这些无限定理成立。

FILES、旧27项与FROZEN去重合并后最终应有38个snapshots。
源/数学review/新script review均进入最终输出的实际hash及canonical bytes/lines记录。
六个review-source pairs分别绑定子族源、480、检查器和476使用的三份证明输入；
已有五对已核，本文落盘后补齐检查器一对。
程序的pair检查是“最终source hash出现在review全文中”，属于机械绑定检查；
其数学实读证据来自独立审查文本，不由该字符串检查代替。

本轮检查现存源及审查中的全部被该regex提取的本地Markdown链接，均有效。
URL scheme与#锚点按代码排除，程序不访问外部网页。
新输出的链接在首次生成前允许指向准确的OUT路径，其他本地目标须已存在。
实际--check还必须读到该已保存输出，因此这个允许不会产生缺失输出的PASS。
没有承诺解析任意复杂Markdown链接语法；当前绑定文本使用该检查器支持的直接链接形式。

## 3. 原S成本、floor与epsilon的精确运算

全部数值运算使用fractions.Fraction；没有float舍入参与判定。
原v=1/8、s=1/20给max(2s,1+4s-4v)=7/10。
V>=X^{1/8}/2所产生的第四次方常数是16；检查器核2^4=16。
它核的是floor成本的精确常数，实际floor适用域由已读数学证明支付。

固定损失epsilon/20+4epsilon/20+epsilon/2=3epsilon/4<epsilon，
与研究源的prefix、divisor和有限dyads费用一致。
17/24-7/10=1/120、norm差1/480、B-17/24=1/168均正确。
(3B+17/24)/4=479/672，(3B+7/10)/4=199/280；
增长尺度余量分别1/672、1/280，均无精度混淆。
完整norm界与差的幂不是程序枚举得到的，它们仍是前述数学前件。

## 4. Affine delta族与最大截断的逻辑

程序把affine量表示为(constant, coefficient_of_delta)，所有系数均有理。
直接重算a_delta=(3/56,-1)，2a_delta=(3/28,-2)，
d_delta=(5/7,-4)，两项成本差=(17/28,-2)。
该差为affine，两个闭端点的值均为正，所以对实际开放域0<delta<3/56也为正。
这只认证成本主导关系，不把delta=0或3/56加入解析定理的允许域。

r0_transfer=(B,-1)认证(3B+d_delta)/4=B-delta。
切换点threshold=(B-c)/4=1/672，d_delta在此等于c=17/24且斜率为-4。
因此threshold左侧取d_delta，右侧取c；两branch分别是B-delta与B-threshold，
共同等于B-min(delta,1/672)。代码已有交点、斜率和两branch精确公式的检查。
输出的domain也明确是先固定delta，不会声称delta(X)趋零时的一致常数。

特例1/280严格在域内，恢复a=1/20、d=7/10及199/280。
特例1/672给sharp=5/96、成本17/24，两次转移均479/672。
sharp-s=1/480、0<sharp<v以及2sharp<c均核准。
(c-1/2)/4=sharp体现单调约束1/2+4a<=c的准确门槛；
在此域2a费用也满足，所以它是该显示成本族内的最大截断幂。
这不是所有算术方法的最优性，也不认证原完整四矩常数或新的whole幂。

本轮没有调用build，而是用AST隔离第87至136行的纯Fraction节点，
在内存执行28个有理断言，全部通过。另写独立公式，在五个固定delta值上核两branch，
覆盖threshold两侧及两规定特例；一般域的结论来自上面的affine推导及数学审查。
最初隔离测试使用分离globals/locals，lambda不能找到b；已将测试器改为同一namespace，
随后完整通过。该测试器问题未涉及被审脚本，未改脚本或任何文件。

## 5. --check只读与输出语义

AST语法检查通过。build只读文件、检查条件并构造内存dict，没有写入调用。
main在--check分支比较json.loads(saved_OUT)与当前完整result；
不一致时SystemExit失败，缺失文件或失败前件也不能返回PASS。
它比较包括全部checks、snapshots、review_pairs、链接数、精确成本和继承比例区间的完整dict，
而不是只比较摘要或PASS标签。JSON对象键序不是逻辑合同，列表次序仍严格参与比较。

唯一写入是第173行OUT.write_text，位于非--check的else分支。
本轮AST检查确认--check分支没有write调用；脚本无子进程或网络执行。
真实独立运行将使用Python -B -X utf8及--check，禁止额外pycache写入。
尚未首次生成时不运行--check成功预测，也不伪造saved JSON。

输出继承旧p_dg有理区间，scope明确不重跑27项旧覆盖、不认证无限均值与Hölder输入，
并保留R_{7/8}/476完整增长前件。
本有限审查未发现实质问题，批准root在两份最终新review落盘后首次生成检查点。
随后应对同一冻结版本执行真实只读--check，stdout/exit另行回报，不回改本文。
