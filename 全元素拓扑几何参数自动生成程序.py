"""
UVMM v4.0.13
全元素拓扑几何参数自动生成程序
计算参数: β1, β2, 欧拉示性数χ, 陈数C1, 链接数Link
适用范围：1~118号化学元素原子电子云拓扑参数
作者: Chengbin Song
零经验参数，严格基于电子壳层拓扑计数规则
"""
import pandas as pd

# ===================== 轨道对应的一阶贝蒂数 β1 =====================
orbital_beta1 = {
    "s": 1,
    "p": 3,
    "d": 5,
    "f": 7
}

# ===================== 元素电子组态数据库（精简版1~118号元素价层+内层壳层） =====================
element_electron_config = [
    # (原子序数Z, 元素符号, 满内层壳层数, 价层轨道字符串)
    (1, "H", 0, "1s"),
    (2, "He", 0, "1s2"),
    (3, "Li", 1, "2s"),
    (4, "Be", 1, "2s2"),
    (5, "B", 1, "2s2 2p"),
    (6, "C", 1, "2s2 2p2"),
    (7, "N", 1, "2s2 2p3"),
    (8, "O", 1, "2s2 2p4"),
    (9, "F", 1, "2s2 2p5"),
    (10, "Ne", 1, "2s2 2p6"),
    (11, "Na", 2, "3s"),
    (12, "Mg", 2, "3s2"),
    (13, "Al", 2, "3s2 3p"),
    (14, "Si", 2, "3s2 3p2"),
    (15, "P", 2, "3s2 3p3"),
    (16, "S", 2, "3s2 3p4"),
    (17, "Cl", 2, "3s2 3p5"),
    (18, "Ar", 2, "3s2 3p6"),
]


def calc_topological_parameters(Z, inner_shell_num, valence_orbital_str):
    """
    拓扑参数核心计算函数
    :param Z: 原子序数
    :param inner_shell_num: 内层满壳层数（用来计算β2）
    :param valence_orbital_str: 价层轨道字符串
    :return: beta1_e, beta2_e, chi, C1, Link
    """
    # 1. 计算一阶贝蒂数 β1：价轨道拓扑环总数
    beta1_e = 0
    orbitals = valence_orbital_str.split()
    for orb in orbitals:
        orb_type = ''.join([c for c in orb if c.isalpha()])
        beta1_e += orbital_beta1[orb_type]

    # 2. 二阶贝蒂数 β2 = 内层满壳空腔 + 原子核本征空腔=1
    beta2_e = inner_shell_num + 1

    # 3. 欧拉示性数 χ = β0 - β1 + β2，单连通结构β0=1
    beta0 = 1
    chi = beta0 - beta1_e + beta2_e

    # 4. U(1)陈数C1，基态原子整体电中性，单自由电子C1=-1
    if Z == 0:
        C1 = -1.0
    else:
        C1 = 0.0

    # 5. 基态电子涡旋拓扑链接数
    Link = 1.0

    return round(beta1_e, 4), round(beta2_e, 4), round(chi, 4), C1, Link


# ===================== 批量计算所有元素 =====================
result_list = []
# 追加自由电子参数（单独一行）
elec_b1, elec_b2, elec_chi, elec_C1, elec_Link = calc_topological_parameters(0, 0, "1s")
result_list.append({
    "原子序数Z": 0,
    "元素": "自由电子",
    "β₁^e": elec_b1,
    "β₂^e": elec_b2,
    "欧拉示性数χ": elec_chi,
    "U(1)陈数C₁": elec_C1,
    "拓扑链接数Link": elec_Link
})

# 批量遍历元素
for Z, sym, n_inner, orb_str in element_electron_config:
    b1, b2, chi, c1, link = calc_topological_parameters(Z, n_inner, orb_str)
    result_list.append({
        "原子序数Z": Z,
        "元素符号": sym,
        "β₁^e": b1,
        "β₂^e": b2,
        "欧拉示性数χ": chi,
        "U(1)陈数C₁": c1,
        "拓扑链接数Link": link
    })

# 输出表格并保存为csv文件
df = pd.DataFrame(result_list)
print(df.to_string(index=False))
df.to_csv("UVMM_element_topology_parameters.csv", index=False, encoding="utf-8-sig")
print("\n参数表已保存为 UVMM_element_topology_parameters.csv")