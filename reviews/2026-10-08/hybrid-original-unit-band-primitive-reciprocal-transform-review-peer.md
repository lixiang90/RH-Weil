# 平方模 primitive 角色逆元变换：不同作者全文审查

2026-10-08，perron_reviewer。只新增此审查；源、旧文件及 Git 未动。
**限定 PASS：准确有限变换成立；不认证 BC 解析节省或任何 whole 改善。**

已 FULL READ 根作者
[188行源](hybrid-original-unit-band-primitive-reciprocal-transform-research-root.md)，
6954 canonical LF bytes，SHA256
4b13bec23ff399739b26003954a28e0d9d889617955bf6e7a43e428ab3a7aa2c。
哈希只统一 CRLF/lone CR 至 LF，不 trim。

本轮另 FULL READ
[246素数腿接口](hybrid-original-high-product-minor-prime-leg-research-checkpoint-audit.md)
（SHA 1790bc3878900e88c89d2ba3b51ba0cf06e85583e353879df0e9a514bfd79b0f），
复核已全文读取并独审的
[337有理切片](hybrid-original-high-product-minor-rational-slice-research-high-product.md)
（SHA 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8）
的实际周期域、共同参数与未付 complement；actual425已在前轮全文读取。

## 1. Fermat quotient 与全部角色

对奇素数 \(q\)，\(Q_q(x)=(x^{q-1}-1)/q\bmod q\)
在 units mod \(q^2\) 上良定义。将代表改为 \(x+q^2k\) 后，
分子只改变 \(q^2\) 的倍数。相乘和二项式展开严格给
\[
 Q_q(xy)=Q_q(x)+Q_q(y),\qquad Q_q(1+qz)=-z\bmod q.
\]
所以源采用
\(\chi_{c,\psi}(x)=\psi(x\bmod q)e_q(-cQ_q(x))\)
恰有 principal-unit 限制 \(\chi(1+qz)=e_q(cz)\)，符号正确。

\(c=0,\ldots,q-1\)、全部 \(q-1\) 个 tame \(\psi\bmod q\)
产生 \(q(q-1)=\phi(q^2)\) 个不同角色。
不同 \(c\) 由 principal-unit 限制区分，同 \(c\) 由 tame 因子区分；
故确实穷尽全部角色。\(c=0\) 正是诱导角色，
\(c\ne0\) 的 conductor 恰为 \(q^2\)，没有遗漏 primitive 角色。

## 2. Gauss 因子的精确符号和零项

写 \(x=a+qj\)，有
\(\bar\chi(a+qj)=\bar\chi(a)e_q(-cj\bar a)\)。
原 additive 因子为 \(e_{q^2}(a)e_q(j)\)，故内和
\[
 \sum_{j\bmod q}e_q(j(1-c\bar a))
       =q\,1_{a=c}\quad(c\ne0).
\]
独立核准
\[
 \tau(\bar\chi_{c,\psi})
       =q\bar\chi_{c,\psi}(c)e_{q^2}(c)\quad(c\ne0).
\]
\(c=0\) 时内和为 \(\sum_j e_q(j)=0\)，包括 principal 及所有
imprimitive 角色。这些 Gauss 项是精确0，未将其作为解析误差删除。

对 unit \(v\)，有限角色正交恰给
\(e_{q^2}(v)=\phi(q^2)^{-1}\sum_\chi\tau(\bar\chi)\chi(v)\)。
实际 \(p,r<q\) 为 genuine primes，\(q\nmid n\)，所以
\(v=-npr\) 确为 unit；源(10)的 G 负号、\(q/\phi(q^2)\)
和全部 \(A_\chi B_\chi\) 权重均准确。

## 3. j 相位与求完 tame 角色后的恢复

源的 \(-a-qj=(-a)(1+qj\bar a)\bmod q^2\)，故
\(\chi(-a-qj)=\chi(-a)e_q(cj\bar a)\)，D 的相位为正 \(cj/a\)。
展开 prime sums 后，固定 \(c\) 的 tame 正交给
\[
 \sum_\psi\chi_{c,\psi}(-apr/c)
       =(q-1)1_{-apr\equiv c\ (q)}e_{q^2}(-apr-c).
\]
这里除以 \(c\) 是 mod \(q^2\) 的 unit inverse。
同余成立时 \(x=-apr/c\equiv1\bmod q\)，
\(\chi(x)=e_q(c(x-1)/q)=e_{q^2}(cx-c)\)；
\(cx\equiv-apr\bmod q^2\)，故最后的相位及符号正确。

它与外 \(e_{q^2}(c)\) 准确相消，且
\(q(q-1)/\phi(q^2)=1\)。每个实际 \(a,p,r\) 唯一决定非零
\(c=-apr\bmod q\)。在这个真实耦合族上
\(c\bar a=-pr\bmod q\)，所以 D 恢复 \(e_q(-jpr)\)。
最后得到 \(e_{q^2}(-apr)e_q(-jpr)=e_{q^2}(-(a+qj)pr)\)，
完整恢复原 G，没有产生一个独立的 inverse cancellation 变量。

## 4. 准确 minor mask、共同参数与范围

337真实剩余同时排除旧 \(d\le W\)、半径 \(W/(dS)\) 的表示，
和新增 \(W<d\le B\)、半径 \(1/S\) 的表示。
两者保留全部整数平移，均只依 \(n/q\bmod1\)；
因此 \(\Omega_q(a)\) 对 \(n=a+qj\) 的周期身份成立，
而 \(d=1,a=0\) 条件已排除 \(q\mid n\)。
这没有改成 \(B/(dS)\) 的另一套 arc 定义。

共同 \(J_q\) 先由 \(\nu\) 的零支撑得到，真实 \(s\) 支持是
随 q 移动而不随 n 移动的 prime interval。
固定共同 Fourier/Mellin 参数后，u、v、z 保留原 prime 权、
twists、dyadic 两端、严格 q-prefix 和同-u profile。
角色身份对这些任意固定准确权及任意有限 j 集合成立；
不完整端period由 \(w_q(a+qj)\) 的实际零支撑保留。
这里没有作取绝对值、signed 域放大、Fourier 尾删项或解析恢复。
\(p=s,r=s\) 尚在主变换内，其原精确修正须按源声明另付。

有限身份因此限定 PASS。角色 prime sums 依赖 c、q、真实产品，
不能将它们视作与 inverse 相位无关的三份系数并消费 BC。
本审查不消费 BC 主定理、L 函数家族输入、新指数、whole 四矩、
常数预算、零点比例或无零边界；这些额外合同仍待独立证明。
