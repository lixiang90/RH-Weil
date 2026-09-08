# 358与Arb核组件：内部独立复核

2026-09-08。只读代理Franklin；沿用用户对本GOAL的长期授权。
这是模型交叉审计，不是外部同行评审或Arb库的形式化验证。

## 核读与结论

核读358全文、radius_five_arb_kernel.py全文、11条smoke记录、
固定profile和运行环境。数学公式及当前冻结输入球算术PASS：

- sinc两阶导数没有遗漏缩放；Taylor32系数与积分给出的33阶余项正确。
- lower/upper/man_exp到Fraction保留向外精确端点；余项上端转半径只会扩大球。
- 90项固定窗口与能量导数吻合，不调用350有限参数域的旧正弦原语。
- 整格宽d对应核二次Taylor余项d³/384正确。

只读复现原11点smoke并截获写入，全部记录一致；另做5参数的15项独立有理
Taylor检查、4项半径检查和宽跨零球接受／拒绝检查。0、6.5209647、640
三点用90位直接密度积分旁证前三个导数及能量导数，均落在球内。
这些有限检查不构成完整表或5D势证书。

## 异议与处理

1. 原实现先验read_bytes()哈希、再read_text()解析，有双读取绑定缺口。
   代理用不修改磁盘的模拟证明第二次读取可不同。主线程改为一次读取raw，
   对同一raw验哈希并json.loads(raw)。实际冻结profile未变化；
   原结果并未因此被发现错误，但严格输入绑定必须修正。
2. 358的“三阶jet”改为“0、1、2阶三分量jet”，没有声称返回三阶导数。

原审查SHA256：

| 对象 | SHA256 |
|---|---|
| 原358 | 3f2b1fb9c472adf7842fd7368b2323c5840e6550d6a637578f0de9d776379967 |
| 原核脚本 | fd2a1c24152cd42fa22dfac44074f86874842aee242f7d1bc2165541934cb0c9 |
| smoke | cfc0b8460137e68f2b9dc97d2fb6e70dba0bcc1c03f5adc8a625c8a15df22c8b |
| profile | 3a89799a5705cc8c30c629643f32d72ee000c34bf67798510d6bfdd8575bdca0 |

修后核脚本SHA256为
d5fbe4cba8ccbf47aed6562b46d18a7fb53f409462f5874850312da978648d05；
Gibbs已用修后版本独立重放77,750核值和全部有限图边。
Franklin已只读复查两处修正，确认全部闭环；
修后358的SHA256为d1f464239d1128cfdb51f75ef8035f9a8572edbc9b7ca51eac818163186ea1d8。

接口语义来源：[python-flint 0.9.0实球接口](https://python-flint.readthedocs.io/en/latest/arb.html)。
代理未重新核验wheel来源、未生成完整表、未派生子代理、未写仓库文件。
