# 反向大值范围审计：独立复核

2026-09-07，Gibbs；主线程整理完整报告的结论、证明核查与修订清单。
全程只读，未修改文件、未派生代理，未接手330/331。
对象：[来源审计](reverse-large-values-source-audit.md)。

**窄范围复核通过。** 点集到测度的桥梁、tau>=2推论、ANTEDB全tau范围反例、
TTY五项的两条凸组合均成立。需要补齐的量词、符号和端点已在来源审计中采用。

1. MT Theorem1.2控制Lebesgue测度，长度T^epsilon<=M<=sqrt(T)/2，
   所有允许M和M'的并集，0<=nu<=1/2。第1页N计重数与正负高度。
   第2页Remark1.3的prime/Möbius余项是T^(2nu+2epsilon)，没有免费使用小余项。
2. 写A0(v)=sum_{M<n<=v}n^(-1-it_r)，则原未加权和
   =M'A0(M')-integral A0(v)dv，绝对值<=3M max|A0|。
   写Ah(v)=sum n^(-1-i(t_r+h))，精确恒等式为
   A0(u)=u^(ih)Ah(u)-ih integral_M^u v^(ih-1)Ah(v)dv。
   因而式(2)正确，端点可以依r,h变化；原定理本身覆盖这一并集。
   固定delta余量吸收常数和N^o，每个半长1/4区间在事件内，一分离保证总测度|W|/2。
3. T'=16max(T,N²)保证M<=2N<=sqrt(T')/2，固定tau>=2时T'=N^(tau+o(1))，
   epsilon<1/(2tau)保证下端长度；tau=2也覆盖。
4. 对固定有限实值连续f，先以eta精度选有限网格，再用N对alpha单调性，
   得N(alpha,U)<<U^(f(alpha)+2eta)，不用f单调。
   选择delta+epsilon<min(delta0,sigma-1/2)，零点项指数为
   epsilon+sup_{alpha>=sigma-delta-epsilon}[f(alpha)+(alpha-sigma+delta)/2]+2eta，
   余项指数(1-sigma+delta)/2+epsilon。先高度极限再消去损失，得到式(3)。
5. ANTEDB Definition7.1/8.1明确允许全部tau，没有隐藏N<=sqrt(T)或T>=N。
   取T=N^(1/8)，积分主项>=N/sqrt(1+4T²)，误差O(1+t)，且T²/N->0；
   最终整个和>=N/(4T)。I=(N,2N]、W=Z intersect [T,2T]、
   V=N/(4T)构成合法pattern，LV_zeta(7/8,1/8)=1/8，除以tau得到1。
   Huxley输入使f(alpha)+(alpha-7/8)/2严格递减，
   sup<=3/13，印刷右端为1/2；矛盾不依赖待否定引理。
6. 精确失效位置在PDF第84页证明首句调用MT Theorem1.2：
   同时省略测度桥梁与长度限制。来源审计修复前者并限定tau>=2。
   tau<2用同一T'会得到N^(2+o(1))，不能继续按原tau归一化。
   原MT定理未被此反例推翻。
7. 设m=max(1,2tau-2)，精确展开：
   F2/2+F3/4+F4/4=3tau/4+5-7sigma；
   2F4/3+F5/3=2tau/3+9-12sigma+(m-1)/3。
   非负凸组合受max Fi控制，得到来源审计的tau0必要上限；SymPy独立展开一致。
   不限制其他大值定理、检测器或归约。
8. 反馈仅指同一sigma直接使用式(3)的数值。右端G_f>=f，但它仅控制LV_zeta；
   LV_zeta<=LV不能反向给一般LV上界，正向零密度关系还需要后者。
   不排除其他独立输入产生改进。
9. 所述MOM的N=X^(3/4)、高度X确有tau=4/3，不直接满足短长度范围。
   扩高到N²=X^(3/2)会改变幂账本；系数转换和有符号响应仍需证明。
   本次未重审238或整个MOM配置。

采用的修订清单：

- I改为每个pattern内共用、可随N变化的I_N。
- 第二次分部求和因子写n^(ih)，加入Ah恒等式。
- f的有限实值、任意固定正误差、网格先固定及损失参数顺序明列。
- A只在alpha<1定义；以左侧上确界与f(1)=0延拓处理终点。
- Definition8.3(iv)改为Lemma8.3(iv)。
- 不循环反馈中显式区分LV_zeta和一般LV。

实际核读：
MT v1 PDF1–9页，尤其2页Theorem1.2/Remark1.3、3–5页结构、6页Lemma4.1、
7–8页测度；未认证10–16页和整篇解析证明。SHA与来源审计一致。
ANTEDB PDF38、45–47、80、83–84、87–88页：定义、反射、11.6证明和Huxley条款；
印刷页号比PDF页序少1。TTY v1 PDF17–18页Theorem32五项；
没有重新启动Thm51补证全审。当前网页也仍列全tau>0。

这是内部范围复核，不是对整个数据库或原论文的认证，也不是新的零密度界。
