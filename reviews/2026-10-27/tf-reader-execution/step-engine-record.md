# 固定 h0 的 physical cosine 原语：实际执行与全 H 误差

2026-10-27；`/root/q0_step_engine`独占执行稿。已恢复README／STATE、check→show、G20261027和execution-handoff。本文只实现同一reader需要的输入原语，不改STATE／cadence／文献库，不换h0／F／L，不建C047或运行T/E。当前q0仍未取得数值。

## 1. 实际执行结果

执行：

```
python scripts/tf_reader_step_certificate.py --output reviews/2026-10-27/tf-reader-execution/step-engine-record.json
```

输入仍为h0=1_[1,2]，原physical L² norm为1。实际在27个dyadic bands、97653个cells上求出了cosine像的有理step系数及其向外标量区间，区间精度为10^−30、sin Taylor odd degree29。第二次最终实现执行耗时约7.823秒；该计时只描述本机此次执行，不是复杂度定理。

输出certificate的exact rational比较证明

\[
 \|\mathcal Fh_0-g_h\|_{L^2(0,\infty)}
 \le\sqrt{0.00046553433164985155\ldots}
 <0.021576245<1/32.
\]

显示小数仅便于阅读；正式上界是JSON中的有理数`true_Hilbert_L2_error_squared_upper`。实际有理step的norm²为0.9998759438158662…，也通过(1−1/32)²≤||g_h||²≤(1+1/32)²的精确一致性检查。系数流SHA256为`9ae2e9aedf9b5179b073e30d5d35958ed89f5c7ca16a2b97a013f1f8a07803fb`。

有限step向量由JSON的各band端点／cell数与脚本的确定性有理midpoint／向外sine算法重建；记录保存流hash与逐band error，而非将近十万个系数误充成原算子的有限matrix。脚本也提供任意有限有理physical steps的pointwise cosine区间求值函数；当前mesh／derivative成本计划仅针对固定h0，未声称同一计划适合任意输入。

## 2. 三类误差都是全 Hilbert 误差

实际cosine像为

\[
 f(x)=\frac{\sin(4\pi x)-\sin(2\pi x)}{\pi x}.
\]

截区间取δ=1/32768、X=4096。近0有|f|≤2，故遗漏L²误差平方≤4δ=0.0001220703125。远端|f|≤2/(πx)，用π>3得到tail²≤4/(9X)=0.0001085069444444…。两项都包含未保留的无限区间，不是离散点上的拟合误差。

在[2^k,2^(k+1)]，k<0时用|f′|≤6π<19，k≥0时用|f′|≤6/x+2/(πx²)≤7/2^k。该band上n个等长cell的真midpoint step误差平方≤M_k²(2^k)³/(12n²)。实际选最小dyadic n使每band该界≤ε²/(2B)，ε=1/32、B=27；总mesh界为0.0002211360703109714…。

每个midpoint的sin先按**精确有理周期**约简至角度[-π,π]，Machin交错arctan给π包围，复用已审的向外定点integer interval运算。odd Taylor degree29按full Taylor degree30（偶项为零）给余项π_hi^31/31!；不是未认证的floating sine。脚本在0、±1/4、1/2、3/4等有理周期点核已知正弦值的包围。最终step系数为区间中点的有理数，系数L²误差平方实际逐cell求和上界约1.766×10^−33。

mesh与系数误差位于同一内部区间，不能把两者平方直接相加。实际使用Young参数1/16：内部总误差平方≤(17/16)·mesh²+17·coefficient²；再与不交的近0／远端tail相加。JSON记录完整有理数并以exact comparison验收≤ε²。

## 3. 已执行成本与更严容差的计划

同一明确计划给出下表；只有1/32行实际逐cell求值，其他行只实际运行了整数cost planner。

| 目标L²误差 | cells | δ | X | 状态 |
|---|---:|---:|---:|---|
| 1/16 | 24253 | 1/8192 | 1024 | 仅计划 |
| 1/32 | 97653 | 1/32768 | 4096 | 已执行并认证 |
| 1/128 | 2094821 | 1/524288 | 65536 | 仅计划 |
| 1/1024 | 134199017 | 1/33554432 | 4194304 | 仅计划 |
| 1/65536 | 824631024515 | 1/137438953472 | 17179869184 | 仅计划 |

这是当前dyadic step表示和粗derivative/tail证书的**充分规模**，不是任意真实reader或q0的必要成本下界。它说明将每次F作用粗暴细化到很小global step误差会迅速变重，但不否定root正在实现的exact lowband-moment／residual组织。未因成本换h0／F／source，亦未运行无证书的q0浮点替代。

## 4. 明确尚未支付的部分

这里只认证Fh0→step的输入原语。Π_F／P／完整G inverse、J区间及true-H residual均未由本文件计算；不能将0.021576245的F原语误差直接当q0宽度，后续B／R0／inverse的误差放大仍须逐项支付。q0目标宽≤1/16尚未达到，原五源T/E/cross表更未计算，Hfin无符号可报告。

脚本及JSON包含实施代码版本／interval依赖版本和逐band证书；源matrices的Γ/contact、properpowers、双pole／du-Dlog仍按原目标保留。此次实际原语是实施证据，不是新的经典正性、primitive RR或成长core/coupling成果，不单计数学轮。最终root对其他执行分支共同消费后决定当前reader的验收或准确停止。
