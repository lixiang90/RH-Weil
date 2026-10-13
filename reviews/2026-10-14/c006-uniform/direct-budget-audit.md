# C006 最后一轮：全源 L² 的实际双 Fourier 核费用审查

2026-10-14。独立恢复 AGENTS、README、STATE/check/show、Goal、C006、D20261014B、533。
实际起始 HEAD `44337d2`。本文件不改 STATE/cadence，不单独计轮。

## 当前结论与实际缺口

本审查支付了全 L² 源域上两类真实 high-scale Fourier 配对的可求和费用：
同尺度r=p^n的source核为 O(r^(-3/2))，不同p幂尺度为 O(p^(-2max(n,m)))。
费用不含g的导数，包含joint carrier/p；不是fixed smooth渐近。

另外核准了analytic resolvent中至少三个低扰动δ的**局部代数尾**，
其夹源乘积是TC，范数O(p^(-3/2))；相邻同尺度two-fast cycle的
q²质量和source余项也可精确分离。
但局部TC尾尚未接到actual角迹的joint cutoff极限，
至多两个δ的finite-cycle aggregate及其零尺度mass抵消亦未支付。
仅凭本文件不能写 `||D_p|| <= C p^(-3/2)`，
也不能声称完整actual角迹的所有≥3δ尾已支付。
没有找到实际D_p不可求和的反例；未知预算不能改写成发散定理。

## 实际 source geometry 与合法组织

物理H=L²((0,infinity),dx)，L=1_(0,1)，H_+=I-L，
`F_p=BFB^(-1)`，`B=I-qU_a`、q=p^(-1/2)、a=logp。
低cutoff为 `K_p=L F_p L`，`R_p=(I-K_p²)^(-1)`。
真实正交Sonin投影为

    P_p=H_+-H_+ F_p L R_p L F_p H_+.

对于实源g，Z_g=A_g*A_g的乘子|g_hat|²偶，故Z_g与真实F_p交换。
在有限实际角块上，source overlap可用下述角组织；
延伸到全部角块的jointlimit属于本审查未支付的域前件：

    E_p,angle(g) ~ 2 Re Tr_low[K_p R_p L Z_g H_+ F_p L].

符号~在此记录有限角组织，不能视为无限low乘积ordinary trace已成立。
真实E_p本身由已付完整source夹心TC trace定义；不能对未夹源各块减无限迹。
Z_g的物理核是

    Z_g(x,y)=c_g(log(x/y))/sqrt(xy),
    c_g(t)=integral g(v+t)conjugate(g(v))dv.

若source相关跨度为W，则L Z_g H_+只连接
`e^(-W)<=x<=1<=y<=e^W`，且 `0<=log(y/x)<=W`。
因此它避开低log半线的红外无限体积。
本冻结W=log(sqrt6)，D=e^W=sqrt6<3<=p，
直接配对两种不同p幂频率时具有严格统一phase gap。

## 实际 high-scale bare核

完整Fourier有operator norm收敛展开

    F_p=(1-p^(-1)) sum_(n>=0)q^n U_(-na)F-qU_aF.

每个高尺度positive-half-line核为 `2cos(2pi p^n xy)`；
operator norm中的q^n被尺度核p^(n/2)抵消，不能另外再乘q^n。
下面保留这真实振幅，因而不是遗漏费用后的假小界。

定义单个配对块

    B_(r1,r2)(g)=Tr_low[(L F_(r1)L) L Z_g H_+ F_(r2)L],
    F_(r)(x,y)=2cos(2pi r xy).

此处仅为有限光滑kernel块，source geometry使其普通积分合法。
以y=e^t x、x从e^(-t)到1、t∈[0,W]改写：

    B_(r1,r2)(g)=integral_0^W c_g(-t) I_(r1,r2)(t)dt,
    I_(r1,r2)(t)=e^(t/2) integral_(e^(-t))^1 integral_0^1
                       4cos(2pi r1 xz)cos(2pi r2 e^t xz) dzdx.

因 |c_g(t)|<=||g||²，核L¹_t界即为source L²费用。
也可把Hermitian合并后的even核压缩到sourceU，Young不等式给相同算子界。
限制到逐patch矩零V只能减小范数，不依赖固定g或有限carrier。

## 同尺度：两个真实端点联合给 r^(-3/2)

设r1=r2=r≥1。cos乘积、z积分及x积分给精确分解

    I_(r,r)(t)= e^(t/2)/(pi r(e^t-1))
                   [Si(2pi r(e^t-1))-Si(2pi r(1-e^(-t)))]
               +e^(t/2)/(pi r(e^t+1))
                   [Si(2pi r(e^t+1))-Si(2pi r(1+e^(-t)))].

两个endpoint必须一起保留；将某一个Si尾单独绝对化会漏掉对角交接的额外费用下降。
第二行两个argument均至少const·r，Si−pi/2=O(1/argument)，
故其L¹(0,W)范数为O_W(r^(-2))。

第一行记A=2pi r(e^t-1)、B=2pi r(1-e^(-t))。
在0<t<=r^(-1/2)时，A−B=O_W(r t²)，B约为rt，
`|Si'(u)|<=min(1,1/|u|)`给

    |I_difference(t)| <= C_W/r.

若rt<=1，还可得C_W t，但不需要消费更强的小区间界。
在t>=r^(-1/2)时，把两个Si都减pi/2，得

    |I_difference(t)| <= C_W/(r² t²).

因此

    integral_0^W |I_(r,r)(t)|dt <= C_W r^(-3/2).           (A)

这是整个冻结L²域上的绝对界；joint carrier选择不能破坏它。
对r=p^n、n>=1，全部同尺度high pair的范数和被
`C_W sum_(n>=1)p^(-3n/2)=O_W(p^(-3/2))`控制。

## 不同p幂尺度：实际support gap给 p^(-2max)

令r1=p^n、r2=p^m、n≠m、n,m>=0。
同样积分给

    I_(r1,r2)(t)=e^(t/2)/pi sum_(sign=±1)
       [Si(2pi(r2e^t+sign r1))
            -Si(2pi(r2+sign r1e^(-t)))]/(r2e^t+sign r1).

因为e^t<=D<p，difference方向没有p幂共振。
两endpoint argument有相同符号，且模长至少const_W·p^max(n,m)；
它们的sign·pi/2主项精确相消。
Si的剩余尾与分母各提供一个p^(-max)，故

    ||I_(p^n,p^m)||_(L¹(0,W))
          <= C_W p^(-2max(n,m)).                        (B)

所有different-scale pair绝对和为
`C_W sum_(k>=1)2k p^(-2k)=O_W(p^(-2))`。
这没有假设其符号，也没有以singleprime结果代替many-prime cross。

## 大移位fulltrace：需要用smooth合并核，不机械逐prolate求和

actual第一order flux里的一部分为q乘
`J_U(logp)=Tr(U_a A_gP A_g*)`。
533已经对fixed smooth g用相位分部积分支付任意p-rate。
若要source L² bound，必须保留source kernel：
Gamma与delta的非振荡核精确相消，delta余项在rho=p exp(t)、|t|<=W
振幅为O_W(p^(-3/2))。smooth低resolvent部分亦可在scaling端点积分。
写R_inf=I+J，J为actual smooth低核。FLJLF的scaling diagonal，
先对放大坐标rho x的低forcing积分两次，得到
`sin(2pi rho x)/(rho x)`乘固定cosine端点row，及O((rho x)^(-2))余项。
该row在x≥1为O(1/x)，其所需导数同样O(1/x)，
所以row/x及一阶导数可积。再对x≥1积分一次，得到
sqrt(rho)乘rho^(-2)，即O(rho^(-3/2))。
整个J核的有限导数界是固定常数，不由逐prolate导数求和引入额外发散。
于是whole source L²有

    |Tr(U_logp A_gP A_g*)| <= C_U p^(-3/2)||g||²,
    |2q Re Tr(U_logp A_gP A_g*)| <= C_U p^(-2)||g||².

这是真实第一fulltrace子项的可求和预算。
不能逐项给每个prolate ζ_j矩阵积分一个double 1/|lambda_j|费用再求和；
该组织会丢实位smooth resolvent的联合正则性。
即使这一q·J子项已付O(p^(-2))，actual flux另有
`Tr(U_a P Z_gP)`与完整return words，仍不可省掉。

## analytic inverse 至少三δ尾：局部TC费用及未付jointlimit

令δ=K_p-K_inf，h(K)=K(I-K²)^(-1)。当p足够大，
actual opnorm ||δ||=O(q)，可在真实K_inf周围按δ展开h至二阶。
记至少三个δ的完整余项为H_3，不截断δ内部的lacunary系列。

每个K_r低kernel的HS范数有统一常数，而opnorm≤r^(-1/2)。
Schatten插值给 `||K_r||_6 <= C r^(-1/3)`。
实际δ的lacunary opnorm展开于是给

    ||δ||_6 <= C sum_(n>=1)p^(-n/3)+O(p^(-1))=O(q^(2/3)).

h的analytic word中，三δ用Schatten Hölder给S_2费用O(q²)，
其余δ用opnorm O(q)，所有fixed K_inf/resolvent因子有界；
小q的analytic几何尾可完整求和。因此

    ||H_3||_op=O(q³),  ||H_3||_2=O(q²).                 (C)

写actual source块M_p=L Z_g H_+F_pL=M_inf+M_δ。
source几何给LZH_+为HS，范数≤C_U||g||²。
M_inf为该HS块乘finite-highband实位F L（HS），所以
`||M_inf||_1<=C_U||g||²`。
`||M_δ||_2<=||LZH_+||_2||F_p-F||_op<=C_U q||g||²`。
由(C)

    |Tr(H_3M_p)|<=||H_3||_op||M_inf||_1
                     +||H_3||_2||M_δ||_2
                 <=C_U q³||g||².

这项局部乘积费用属于whole source L²，没有使用source导数。
它还不能消费为actual E_p无限word尾：
actual角分解首先给source完整overlap trace，未给任意分离角项的absolute trace。
`A_g R_p A_g*`为TC不自动推出`A_g|R_p|A_g*`为TC，
也不自动保证角谱截断后的每个分离tail trace收敛至同一值。
需要把该analytic H_3乘积接到原actual角jointcutoff的合法极限；
本审查没有完成这一步，因而不把(C)升级为完整≥3δ trace预算。

## 相邻two-fast cycle：精确mass与uniform remainder

令K_r=L F_(r)L，L_r=1_(0,r)、H_r=I-L_r。由实际cosine scaling代数有

    K_r²=r^(-1)L F L_r F L
          =r^(-1)[L-L F H_r F L].                      (D)

因此相邻同尺度return的r^(-1)质量是准确算子身份，不是猜测。
若M是M_inf或固定smooth低resolvent dress后的M_inf，
其kernel M(z,x)在第一个低坐标z光滑至端点，另一低坐标x有界；
所需z导数和S_1范数被C_U||g||²控制，不要求g导数。
对z积分分部积分，

    (F L M)(w,x)=M(1,x)sin(2pi w)/(pi w)+O_U(||g||² w^(-2)).

于是(D)的frequency-tail trace只需控制
`integral_r^infinity sin(2pi w)cos(2pi wx) dw/w`。
这为频率1±x的两个Si尾；其x∈[0,1]的L¹范数≤C log(2r)/r：
在1-x<=1/r的角区用有界Si尾，外区用1/[r(1-x)]。
剩余w^(-2)项积分为O(1/r)。因此

    |Tr(K_r² M)-r^(-1)Tr(M)|
          <=C_U ||g||² log(2r)/r².                    (E)

可以先对frequency r<w<R取合法HS夹心迹，再令R趋∞；
bounded operator强收敛与M的S_1域固定实际trace，Si核的L¹界支付极限。
所以(E)没有逐个相减未经源夹心的无限迹。
对r=p，这明确给q²固定质量系数和可求和O(p^(-2)logp)source余项。
它不覆盖任意nonadjacent两个δ或h_1M_δ的one-sided smooth dress。

## 完整逆的零尺度问题：本审查未支付的一步

bare high/high配对(A)、(B)不能直接取代K_pR_p。
完整R_p虽然opnorm有统一晚p界，但将它与上述source kernel作粗乘积
不能维持source L² trace-map bound；这里不是普通bounded operator norm乘法问题。
上面的(C)只支付至少三δ的局部TC乘积；
actual source jointlimit仍需证明，以下0/1/2δ finite cycles也仍有缺口。
具体有两类尚需合并的项：

1. Fourier n=0系数(1-1/p)与低反向项 `-p^(-1)F_(1/p)`
   在bare pair中产生O(1/p)的smooth零尺度核。
2. 高频两次返回在Gram/resolvent中产生相反的q²质量块。
   531/533已说明bare q²mass在完整projection里精确取消，
   但这不自动给每个whole-source trace-kernel word的统一求和。

删掉第2类会错误地留下unsummable 1/p核；
仅凭第2类取消的抽象statement又不能免费将(A)/(B)推广到任意长word。
需要一个actual source-kernel class，在resolvent乘法及全部cross下闭合，
并控制这些有限nonzero-scale cycles的可求和范数。

合法的后续取消方式可以是：先证明完整resolvent的nonzero-scale核
uniform O(p^(-3/2))，而零尺度部分为p^(-1) times固定bounded smooth source核
加uniform O(p^(-2))。533在稠密smooth域给pD_p趋0，
便严格迫使那个固定零尺度系数为0。
这一步必须先有uniform核分类，不能只由dense pointwise渐近猜norm收敛。
本审查没有完成至多二δ的全部finite-cycle class或其与actual角jointlimit的前件。

## 消费判定及唯一下一动作

新增独立工具是(A)/(B)真实source块的统一、无需导数、可求和绝对费用，
actual q·J_U子项、(C)局部扰动尾TC及(D)/(E)相邻return质量/余项。
full inverse缺口是有限cycles和actual jointlimit，
不是已证uniform可求和全预算。它不重做已排除的uniform norm首项渐近。
单靠本文件，whole V 的 `sum_p||D_p||<infinity` 仍是open。
没有证明不可求和，也没有将bare q²块或toywindow交接当成actual反例。

本轮停止：C006第二且最后一轮仍未支付whole V的single-p norm求和，
不继续给unknown word预算改名，不先扩S/U。
重新准入须实际finite-cycle aggregate、closed source-kernel预算及jointcutoff域证明，
而不是增加N、fixed-g余项或generic relativeGamma。
宏观可继续的不同动作是532新桥已经定位的真实`QW-T2=-E2`低域signed比较；
具体唯一主合同及下一动作由主代理在STATE结算，不由本辅助文件创建。
本辅助审查无待处理进程，不独立计研究轮，也不支持Goal完成声明。
