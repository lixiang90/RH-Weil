# C010：原已认证whole head的单次odd ceiling准入检验

2026-10-14；已恢复AGENTS/README/STATE/check/show、当前C010、Goal和D20261014I。
新预注册：[full-head-odd-preregistration.json](full-head-odd-preregistration.json)。
本次使用C009原已完全认证的448 Legendre degrees，其中odd sector224个coordinates，
不是扩C001/pilot N。80dps不增加，不用ζzero或外部candidate，不改旧证据/STATE/cadence/git。

## 冻结对象、一次提案及exact source

实际对象仍是R=M+K+U，L=17/16，Lebesgue norm，dual pole及全部primepowers不删。
输入hash重核为

- source-matrices.json：`4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac`；
- tail-columns.json：`2a88894c7405e01a37cbdef8671e9d628ddc60ae9cdb335fa2636fe49b6666a2`。

自写脚本[scripts/c010_full_head_odd_ceiling.py](../../../scripts/c010_full_head_odd_ceiling.py)
读取原A/J₀/tail raw数据，取orders1,3,...,447，按Γ_nn=2L/(2n+1)作两侧归一化：

    R_head=Γ^-1/2[A_raw+J0_raw+(648/17)(r0r0^T+r1r1^T)]Γ^-1/2.

没有再乘L²到J₀。ordinary80 Cholesky仅作proposal factor，8次inverse iterations
从本辅助已有odd64诊断向量zero-pad开始；这不是eight次N扫描或独立全谱认证。
其最后ordinary Rayleigh为1.68367899690034718436...e−31。
将raw polynomial coefficients固定为50 significant decimal的exact rationals，保存
[full-head-odd-source.json](full-head-odd-source.json)。
原稿第一次运行因mp.matrix(dim)产生square而非vector使求解赋值退出，
在任何inverse iterate产生前修成mp.matrix(dim,1)，同一参数/bytes再跑exit0。
该实现纠错没有改变proposal范围或静默扩大预算。

## 支付源误差后的严格Rayleigh ceiling

冻结源为real odd polynomial zero-extension

    f(u)=1_(-L,L)(u)Σ_(n=1,3,...,447)c_nP_n(u/L),
    N_f=Σ_n c_n²Γ_nn>0.

它属于closed logarithmic form域；对bounded R更无需smooth源域假设。
Cc∞ core可在需要时给合法smooth逼近。提案eigensolve是否精确不影响这个确切source的Rayleigh界。
以Fractions计算完整raw head quadratic及rank-two U update，并支付

    εR=εA+εH+σ=2^-204+2·2^-220+9·2^-512≈3.88950324326e−62.

因此

    <f,Rf>/N_f ≤ q_center/N_f+εR ≤ c_odd,

其中c_odd保存为向上256-bit dyadic，见
[full-head-odd-result.json](full-head-odd-result.json)，其decimal值为

    c_odd=1.68367899690034718436283137127064234361238487646...e−31.

strict comparison的基准为已逆审actual even source上界

    u=7954159549289785371664718615168914673915149/2^256,
    s=10^-34.

Fraction结果：c_odd<u为false；c_odd+τ<u为false；c_odd<s为false。
这里τ=2^-49162，所有比较都在exact rationals中执行。

## 消费结论和唯一下一门

此次**没有找到**指定R odd Rayleigh ceiling低于u或s的见证，
所以不交付固定supplier/upper路线的失败定理；也不据此宣称whole odd lower成立。
一个严格ceiling高于阈值无法排除其他source更低；ordinary factor或inverse-iteration
稳定不能替代全source inertia/补空间符号证书。
结果也不是Q的upper、负Q test、C009反例或所有ground排序方法的边界。

唯一下一动作：主代理在同一原whole head与paid complement预算上检查s=10^-34的
真正odd lower准入门及第二even门。若其完整finite sign/error链未付，simple-even仍open；
不继续N/dps扫描或以此次ordinary positive head当下界。
自写脚本已exit0，无本辅助pending process，不另计研究轮。
