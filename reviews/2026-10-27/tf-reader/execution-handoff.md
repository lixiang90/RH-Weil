# 固定五源reader：下一次实际执行位置

2026-10-27。本文只把已闭的计算前件变成唯一实施动作，不新建数学合同／轮数，不改L/j/F或Hfin。五源T/E表、原norm及crossblock仍是完整待交付；下面的单输入是reader实现的必要验收，不替代五源目标。

## 唯一下一动作

实现带误差的physical step-vector reader，并对**固定**h0=1_[1,2]（原physical L² norm1）计算

\[
 q_0=\langle h_0,F\Pi_FFh_0\rangle
 =\langle v_0,\mathcal A^{-1}v_0\rangle,\quad
 v_0=PB_F^*Fh_0,\quad
 \mathcal A=PB_F^*B_FP+(I-P).
\]

F仍为八个base primes，P/cosine/source规范与root总稿完全相同。初始Fh0有明确函数[sin(4πx)−sin(2πx)]/(πx)，其双端尾按原稿付款。h0是输入reader验证向量，不是新的physical源或新的正性假设。

必须输出真实Hilbert范数残差证书与J的rounding区间：取一个明确的实际trial z，r=v0−mathcalAz，J=2Re<v0,z>−<z,mathcalAz>，则q0∈[J_low,J_high+||r||²/d]∩[0,1]，d=∏_(p∈F)(1−p^−1/2)²。不能用finite section残差或浮点solve成功状态代替这里的norm。

第一次验收的固定目标是总enclosure宽度≤1/16。一组足够预算是J半宽≤1/128、真实||r||²/d≤1/32，给总宽≤3/64。记录实际step划分、两端cutoff、C_N/R_N精度、source-free operator action误差、trial及inner-product误差。global谱尾只作保底；若用更好trial，也必须以实际全Hilbert residual验收。

先输出一份操作成本／误差参数表；若证书要求超出当前可执行成本或仍缺实际函数的误差实现，保存确切项和已有代码／日志，不将抽象收敛式当作q0数值。不得偷偷换h0或删掉不利tail以让验收通过，也不串另一reader／paper。

q0通过后，沿**同一**实现扩到D_r有限rank所需compression，完成原冻结五源Ndu/NDlog/Q/T/E及core/cross误差表。源表linear-first与column全transpose约定必须同时执行；本五族可用已证明real symmetry，但不能删一般complex责任。所有powers/poles保定义。

## 未执行与禁止升级

本次只有C0精确有理gap脚本已执行；h0/q0程序、compression残差和五源表均未运行、无数值可报告。Hfin:E≤0只在那五源上待检；可靠正Rayleigh可反驳，pass不代全源／成长／RH。实现成本上界也不是actual signed误差的必要下界。

若不能产出有信息的认证表，本冻结计算预检止于具体成本／误差，不增j、换L/F或把unknown remainder改名C047。数学主瓶颈仍为实际全源／成长signed core/coupling及独立primitiveRR；whole4/5UPPER未变，长期Goal保持open。
