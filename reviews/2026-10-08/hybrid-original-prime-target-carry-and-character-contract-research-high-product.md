# 真实外素数目标的 carry 匹配与角色合同边界

2026-10-08，high_product_joint。研究轮5，基线 main 84670bc。
只新增本源，不改冻结输入、输出、检查器或 Git。待不同作者全文审查。
本稿证明精确有限匹配公式，识别带 F 的一阶算术输入；没有新省幂。
旧191已给 quotient/remainder 与 Taylor 展开；下述配对是该工具的显式展开，
不把重新展开当成新增付款。

## 1. 冻结实际对象

此前均已 FULL READ；本轮重读191全部、重核其余身份。canonical LF不trim。

| 输入 | SHA256 |
| --- | --- |
| [actual425](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [共同mask337](hybrid-original-high-product-minor-rational-slice-research-high-product.md) | 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8 |
| [coherent191](hybrid-original-coherent-period-energy-research-checkpoint-audit.md) | fe19e50f955c47b7abb22933d0b406a9bc339ac68056d8d115d1f7277be22c5f |
| [mixed228](hybrid-original-mixed-prime-continuous-legs-research-checkpoint-audit.md) | 7716f0b9452914f24e321fe9bd4d76e1e63d1cae0b31a01e18b761a5f58f8a87 |
| [494](../../notes/494-original-double-deviation-and-upper-cauchy-core.md) | 6abe8a6ddc66178a4f67352ee8cb4138622c8bd78a103dea377f98513c7e839c |

保持原 \(X,L,b_p\)、真实最大prime \(q\)、全部 \(s,p,r<q\)、
dyadic \(PR\asymp QS\)、sharp endpoints、same-\(u\)、\(g,\nu\) 与 floors。
先由 \(\nu\) 零支撑得到共同 \(J_q\subset(0,q^2)\)，才作原公共参数分离。
固定参数 \(\lambda\)，先不删 \(p=s,r=s\)，定义
\[
 F_q(a)=\sum_{s\in\mathcal S_q}c_s e_q(as),\quad
 G_q(n)=\sum_k C_{q,k}e_{q^2}(-nk),\quad
 C_{q,k}=\sum_{pr=k}b_pb_rp^{it_p}r^{it_r}.
\]
\(c_s\) 含原 \(b_s(s/S)\) 和固定twists，真实 \(\mathcal S_q\) 与 \(n\) 无关。
内prime腿保留严格 \(q\)-prefix；\(0<k<q^2\)，每 \(k\) 至多两个有序factor pairs。
以下恒等式只对这份 unmasked 原子系数写；不伪造一个与 \(s\) 无关的删除系数。
191§6对实际同mask直接重推的正付款，恢复三项 \(s\) 排除共 \(O(\sqrt X L^C)\)；
原 graph、nn、chirp 的完整已付桥仍保持原范围。

## 2. 零 \(\nu\)-twist的精确 prime-target 配对

取原完整period的共同 \(j\)-窗 \(I\)，暂令 \(t_\nu=0\)。
写唯一 \(k=qz+v\)，\(0\le z,v<q\)，定义
\[
 D_I(v)=\sum_{j\in I}e_q(-jv),\quad
 B_{q,z,h,I}=\sum_{v<q}C_{q,qz+v}D_I(v)(v/q)^h,\quad
 \widehat\Omega_{q,h}(b)=\frac1q\sum_{a=0}^{q-1}
 1_{\Omega_q}(a)(a/q)^h e_q(-ab).
 \tag{1}
\]
在 \(h=0,a=0\) 处取 \((a/q)^0=1\)。
原minor的 \(\Omega_q\) 排除 \(a=0\)，且不依赖 individual \(s\)。
完整慢相位展开的 absolute factorial 和为 \(e^{2\pi}\)；有限求和可逐项交换。
故准确有
\[
 \mathcal J_{q,I}^0:=\sum_{a\in\Omega_q}F_q(a)\sum_{j\in I}G_q(a+qj)
 =q\sum_{h\ge0}\frac{(-2\pi i)^h}{h!}
       \sum_{s,z}c_s\widehat\Omega_{q,h}(z-s)B_{q,z,h,I}.
 \tag{2}
\]
证明只需 \(e_{q^2}(-nk)=e_q(-az)e_q(-jv)e(-av/q^2)\)
及完整 \(a\)-Fourier公式；所有实际 prime 和 carry 层均未删。
作为有限代数检查，若**形式取全部 \(q\) 个 residues**，则 \(h=0\) 项为
\[
 q\sum_{s\in\mathcal S_q}c_s B_{q,s,0,I}
 =q\sum_{s\in\mathcal S_q}c_s\sum_{v<q}C_{q,qs+v}D_I(v).
 \tag{3}
\]
因 \(s,z<q\)，没有 \(z\equiv s\pmod q\) 的额外 aliases。
这是一个Taylor项的准确身份，不是完整 \(\mathcal J\) 的值或上界。
形式的全residue测试也不把已付完整nn块转成任意子mask的免费加回。
若仅取全部非零residues，(3)还须减去 \((\sum_s c_s)(\sum_z B_{q,z,0,I})\)。

## 3. 角色读取余数，外 F 匹配整数商

实际 \(v=pr\bmod q\ne0\)，所以 \(\chi(v)=\chi(p)\chi(r)\)。
对完整窗内的 \(j\ne0\pmod q\)，有限 Gauss 身份准确给
\[
 e_q(-jv)=\frac1{q-1}\sum_{\chi\bmod q}\tau(\bar\chi)\chi(-j)\chi(v).
\]
但(3)的外素数目标读取 \(z=\lfloor pr/q\rfloor\)。
把 \(c_z\) 再作乘法群变换时出现的是
\(\chi(pr\bmod q)\psi(\lfloor pr/q\rfloor)\)，不是三个prime角色和的乘积。
由 \(pr=qz+v\) 不能将后一carry因子写成 \(\psi(p)\psi(r)\)。
标准complete Jacobi/ratio恒等式没有交付这个整数商；
在 actual \(\Omega\) 下，还须保留(2)的完整 \(\widehat\Omega_{q,h}\) 卷积。
主 \(j\)-角色的辅助付款没有因此变成整个nonprincipal budget的节省。

## 4. 原 \(\nu\)-twist与端周期必须恢复

实际唯一 \(n\)-twist是 \(w_{q,j}(a)=((j+a/q)/X)^{it_\nu}\)。
把共同 \(J_q\) 按 \(n=a+qj,\ 0\le a<q\) 分组，
令 \(\Omega_{q,j}\) 为实际mask与该period的 \(J_q\) residue区间之交。
完整period的mask为 \(\Omega_q\)，至多两个端period保留自己的区间。
对实际非零 \(n\) 定义
\[
 \widehat\Omega_{q,j,h}^{\,w}(b)=q^{-1}\sum_{a\in\Omega_{q,j}}
   w_{q,j}(a)(a/q)^h e_q(-ab),\quad
 B_{q,z,h,j}=\sum_{v<q}C_{q,qz+v}e_q(-jv)(v/q)^h .
\]
同一展开严格给整个共同 \(J_q\) 的
\[
 \mathcal J_q(\lambda)=
 q\sum_{h\ge0}\frac{(-2\pi i)^h}{h!}
   \sum_j\sum_{s,z}c_s\widehat\Omega_{q,j,h}^{\,w}(z-s)B_{q,z,h,j}.
 \tag{4}
\]
\(n=0\) 不在实际mask中，故不定义 \(0^{it_\nu}\)。
不得以(3)替换(4)、将 \(w\) 塞入私有prime系数，或只估完整period而丢端周期。
191的vector Abel及原 \(\nu\) weighted Mellin合同只恢复已证正能量；
没有把零twist的任意signed prefix估计自动升级成(4)的上界。

## 5. 连续减项与真正一级输入

\(\Delta\mu\) 含连续负measure；Dirichlet \(\chi\) 没有对实数 \(p,r\) 的
canonical定义。对continuous \(pr\)，沿整数 \(j\) 投影所得是有限三角多项式，
其 Gauss 因子化为 \(\chi(p)\chi(r)\) 的证明不成立。
494只在**恢复后的完整带 F signed联合层**给
\(K_{\Delta,\Delta}=K_{\rm pr}+O(L^C)\)；
不能据此声称每个非局部 \(\chi\)-投影或fixed-parameter centered能量已付。

令 \(\mathcal T(\lambda)=\sum_{q\sim Q}b_q\omega_q(\lambda)\mathcal J_q(\lambda)\)，
其中 \(\omega_q\) 保留原 \(Q/q\) 及 \(q,u\) 的bounded公共因子。
原box恰由 \(S/(QX)\) 与共同参数积分恢复此一级signed统计。
191给完整period \(|\mathcal T|\ll(1+|t_\nu|)Q^2L^C\)；端周期旧界同费，
恢复后仍只有 \(QS/X\)。以下是尚未付的、可消费的更弱旁路：
若同一全部参数正包络下的完整(4)统计满足
\(\int W(\lambda)|\mathcal T(\lambda)|d\lambda\ll Q^2X^{-r}L^C\)，
则本box费用为 \(QS\,X^{-1-r}L^C\)，并另保留 \(s\) 排除的旧 \(\sqrt X\) 费用。
在 \(Q=X^u,S=X^w\) 上跨过 \(5/7\) 需 \(r>u+w-12/7\)；
只给部分period或仅(3)不满足这个完整合同。
该一级输入尚未证明。没有新实际省幂、whole、中心常数、比例或无零边界。
