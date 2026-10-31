# 新 retained-tail head 正性与完整 Weil 型的448维后果

2026-11-01；G20261027/runtime1793085111，原冻结基线0c4f。由预先冻结的 NEW Cret 输入门取得严格新符号证书；原C0/P0/v、C058和C066预算均未重开。实际80570退出0，用时248.6810276秒。本文的数学消费以本轮独立终态审查和root收据为准，不把机器PENDING_ROOT或文件存在当验收。

## 对象、规范与结论

令 I=(-9/8,9/8)，H=L²(I,du;C)，p_j(u)=P_j(u/L)，g_j=9/[4(2j+1)]，e_j=p_j/sqrt(g_j)，E:C448→H为等距嵌入。所有函数零延拓。记 f_a=Σa_jp_j=Ex；原源读出 r_a=e^(u/2)f_a。原矩阵范数是

    ||f_a||du²=a*D a=||x||²=∫e^-u|r_a(u)|²du,
    D=diag(g_j).

这里不把||f_a||du与||r_a||du相等。Q_W(f)始终指595完整桥在此半密度规范下的完整经典Weil型，含完整Gamma/contact、pp2,3,4,5,7,8,9与双pole。有限多项式零延拓是compact BV，属于已付Dlog及本次R列的operator domain。

保原 tau=2^-49162、Omega256、eta1、Llow=M+Kcompact+U_old，R=Ttail-tau I-U_old>=0。已root消费的新全H值源是 V=RE、G=E*V>=0，G不是V*V或旧inverse-M Gram。标准shorting给 Uret=V(I+G)^-1V*<=R。定义

    Cret=E*(Llow+Uret)E=C0+G(I+G)^-1G.

本轮严格结论为：对全部x∈C448，

    x*Cret x >2^-205||x||²                 (x≠0).             (1)

从而对全部非零f=Ex，完整Weil型满足

    Q_W(f) >(tau+2^-205)||f||du².                              (2)

这是固定448维子空间上的全复源结论，不是全部H/Dlog的9/8窗口正性，也不涉及无界L或通常Xi。

## 源误差、精确合同变换与真实运行

旧accepted A/J0和896尾坐标给C0hat，native误差

    epsC=2^-204+2*2^-220+9*2^-512.

旧尾坐标仅承担C0的head误差，不给新的全H函数。新SAME-center Ghat满足||G-Ghat||<epsG=2^-203。旧/新h中心不假设精确抵消。由I+Ghat>=(1-epsG)I和非交换resolvent identity，f(G)=G-I+(I+G)^-1的误差<3epsG。因此精确中心Chat距真Cret的native误差<epsSrc=epsC+3epsG<beta=2^-201。

Raw Graw=D^(1/2)Ghat D^(1/2)。令S=Graw+D>0、B=D^-1S，精确有

    Chatraw=C0hatraw+Graw-D+D S^-1D,
    K=B*Chatraw B=B*(C0hatraw+Graw)B-Graw-Graw D^-1Graw,
    T=B*DB>0,
    K-beta T < B*Cret_raw B < K+beta T.

代码直接以整数进行三次矩阵乘法，每区K的公共分母为81*2^1792；不求逆、不使用浮点谱。随后1024位有向区间Schur/LDL直接包围精确K±betaT。完整数学、缩放及有限算术证明见[准入](../reviews/2026-11-01/retained-tail-signed-head/math-admission.md)与[算法](../reviews/2026-11-01/retained-tail-signed-head/algorithm-design.md)。

最终代码23940字节/SHA ed32fa2749c11c1dd1adae3bb078a331c5206a9d79f975a23c45e7df5f2fb7c3经数学与协议独立审查、root18150项隔离有理数/合成对照后，冻结一次1800秒/8MiB预算。实际248.681秒退出0。22输入/审查pins、self/freeze及完整日志均重核；even upper224/lower224、odd upper224/lower224共896个pivot全部严格正，没有提议负见证。输出642941字节，无part/tmp，未重跑。

所以两个lower目标K-betaT均正定，即Chat>beta I。真实误差比beta小，给

    Cret >(beta-epsSrc)I,
    beta-epsSrc=2^-204-2^-219-9*2^-512 >2^-205.

这支付(1)的量化余量，不需从pivot值推测特征值，也不新增数值测试。机器pivotLog.closed字段因not handle.closed写反而为false；原件不改，实际exit0、finish/close/rename路径、完整896行/bytes/SHA及无partial经外部重闭。该标记不承担数学或进程权威，详见[限定纠正](../reviews/2026-11-01/retained-tail-signed-head/pivot-log-status-clarification.md)。

## 最强可消费后果及未付whole责任

旧595的同对象分解给Q_W=Llow+tau I+R，故Q_W>=Llow+Uret+tau I，推出(2)。在head上更精确地，

    E*Q_W E=C0+tau I+G
            =Cret+tau I+G(I+G)^-1.

最后一项非负。此恒等式保留未用的正尾，不把它删掉后反推Q负。

相对强旧，537的全源17/16支持窗不包含这些9/8多项式源；595旧P0失败、旧单点Llow正性及R tinyfloor均不蕴含本次全部448维结论。新增实际G与严格中心符号首次支付本对象的head门；只计一个数学责任，不将head与有限Q推论分成两轮。

Whole Lret仍须支付X=(I-P)V的有利相关、M10/B_M-A_M²及实际混合MV/CX或inverse数据。1.774...补空间HS范数是对象大小，不是误差；当前norm traces不等于完整交叉Gram。原whole-U近似source费<2^-193是充分上费，不能无声用本次2^-205余量吸收，也不是不可改善的必要损失。

因此whole9/8正性、principal/sections/mixed、成长core/cross/Xi和whole leading4/5负惯性UPPER仍未改变，三个长期Goal完成门保持open。下一仅进行一个针对真实whole Schur的前件/误差准入比较，先证明新数据能改变选择，再决定是否值得额外源计算；不自动续精度、方向、rank、eta、窗口或旧预算。
