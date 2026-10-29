# 602：固定源窗全 L² 单位球的实际单素数全返回费用

2026-10-29；C065，一个完整数学迭代。G20261027/runtime1793085111，原冻结0c4f不滚动。两独立证明16385/13097、不同终审16049及root全文消费；具体原字节与前件闭合见[消费记录](../reviews/2026-10-29/onebody-full-returns/root-consumption-scope.json)。

## 定理与实际对象

固定有界log源区间I，S_I=L²(I,du)。H=L²((0,∞),dx)，U_a f(x)=e^(-a/2)f(e^-a x)，A_r=∫r(a)U_a da。P为实际实位Sonin投影，B_p=1−p^(-1/2)U_logp，Π_p=B_pP(PB_p*B_pP)^(-1)PB_p*，使用完整Gram逆。𝒦_{p,I}为532/560的同一source compact误差，𝒦_{0,I}为empty-base误差；它们不同于物理低cutoff压缩C_p=LF_pL。

存在仅依固定实位压缩谱隙的pκ，且对每个I存在有限C_I，使全部p≥pκ有

    ||𝒦_{p,I}−𝒦_{0,I}||_{S_I→S_I} ≤ C_I(1+log p)/p。

这个阈值不依I；C_I可以对窗宽恶劣增长。量词覆盖全部复源单位球、任意频高及在I内随p/X改变的源，常数不含源导数。先在smooth/Dlog使用普通夹源迹，再连续延拓source紧型；不宣称裸L²中两个正迹分别有限。

实际迹差仍为

    t_p[r]−t_0[r]=−𝒫_p[r]+⟨r,(𝒦_{p,I}−𝒦_{0,I})r⟩。

𝒫_p含全部proper powers和原权；只有logp>diam I时其相关全部exact为零。定理对compact误差本身不需要此条件，也覆盖可见p。Γ=2θ′/原FP-contact、全部pp及完整目标的双pole按560原身份保留。

## 全返回证明的短链

令W=diam I。酉log坐标中把source平移到[0,W]不改A_r*A_r及原du范数，令E=1_[0,W]、L为负半线、H_+=1−L，精确有

    T_r=L A_r*A_r H_+=(E A_r L)*(E A_r H_+)，
    ||E A_r L||HS²=∫₀ᵂ a|r(a)|²da，
    ||E A_r H_+||HS²=∫₀ᵂ(W−a)|r(a)|²da，
    ||T_r||S₁≤W||r||du²。

这是无source导数的关键新输入。返回x坐标，T仅连[e^-W,1]×[1,e^W]，核χ_r(log(x/y))/√xy连续有界，不对χ_r求导。

实smooth源使用535/c007已付完整overlap普通迹

    E_p[r]=2ReTr_L[h(C_p)T_r F_pL]，h(C)=C(1−C²)^(-1)。

实位C₀=LFL满足κ=||C₀||<1；D=F_p−F、N=LDL皆op O(p^-1/2)。对全部返回做真正resolvent Taylor，R_σ=(1−σC₀)^(-1)，

    Dh[N]=½Σ_(σ=±1)R_σ N R_σ，
    (E_p−E₀)/2=ReTr(Dh[N]T_rFL)+ReTr(h(C₀)T_rDL)
                 +Oκ(W||r||²/p)。

第一trace循环后振幅为(R_σT_rFLR_σ)(y,x)，输入x的一阶导数由固定F和R_σ=1+smooth核提供；第二trace的输出x导数由h(C₀)提供。二者都不借源导数。实际opnorm收敛级数为

    D=−p^-1 F₁+(1−p^-1)Σ_(n≥1)F_(p^n)−p^-1F_(1/p)，
    F_λ(x,y)=2cos(2πλxy)，||F_λ||op=λ^-1/2。

S₁测试合法取级数trace。低方形在y≤1/λ直接估计，其余一次x分部给(1+logλ)/λ；第二矩形y≥1给1/λ。低/reverse核前系数1/p，实际有限矩形直接估计。Σ_n(1+nlogp)/p^n=O((1+logp)/p)，余项已付1/p，得实源统一型界。实际实结构使r=a+ib的型为a、b两型之和，再凭532/560紧型和smooth密度延拓到全复S_I，得真正operator norm。

## 同一whole对象净后果

定义实际empty-base onebody部分

    𝒦_≤1(X,I)=𝒦₀,I+Σ_(p≤X)(𝒦_{p,I}−𝒦₀,I)，
    𝒦_J(X,I)=𝒦_{F_X,I}−𝒦_≤1(X,I)。

有限p<pκ由旧每p有界紧型吸收，Chebyshev部分求和给Σ_(p≤X)(1+logp)/p=O(1+logX)，故

    ||𝒦_≤1(X,I)||≤C_I(1+logX)，
    ||𝒦_{F_X,I}−𝒦_J(X,I)||≤C_I(1+logX)。

这是整个fixed-I源算子的绝对费用及差范数，不是新𝒦_J正号。无需把p≤e^W整个可见集合列为未付head。

## 强旧扣除、停止及长期门

533已对每个fixed compact smooth源给p^-2 A[r]+O_r(p^-5/2)及绝对可和，含源Sobolev费；534的whole范数降级不撤销它。533＋585/589的j_X=t_X+O_r(1)、ratio1，以及极化533＋587的全部fixed finite-E共同lower/正谱后果，均属old0。本轮不重计这些结果。原4340及post601/AK关于固定smooth rate未付/其归因新增的诊断冻结，原件保留，纠正见同目录533-fixed-source-scope-correction。

本次不同责任是无导数、整个固定窗单位球的完整norm上界。旧534的子项S₁/HS和535的smooth全trace没有闭合这一统一责任；新HS×HS与正确坐标核估计一次合成它。不能从充分上界的不可和性推出actual norm和发散，也没有uniform p²渐近。

C_I成长、自然coupled I_L/F_L、危险signed core/cross、𝒦_J有利抵消、principal/sections/mixedRR与通常Ξ均未付。Whole leading4/5仍是旧负惯性UPPER，未改善。局部whole-onebody费用瓶颈已闭；长期关键瓶颈未改变，三Goal门open，同一运行Goal保持active。C065预算耗尽，不自动续single-p rate/参数/窗宽/一般base或新来源合同。原cadence仅一次3→4/history65→66/latest602/formal20保持，之后才有资格及时宏观21；复盘另为0数学轮。
