import pyautogui
import time
import pyperclip

class This_is_shxtbox:
    @staticmethod
    def main():  
        contact_list = [

            # ("LJX2894563982", "祝您新年快乐呀"),
            # ("Hamilton8090", "祝您新年快乐呀"),
            # ("infinite-passion", "祝您新年快乐呀"),
            # ("engxisu", "祝您新年快乐呀"),
            # ("naige47", "祝您新年快乐呀"),
            # ("Franky_x_", "祝您新年快乐呀"),
            # ("Serendipity-_-3166", "祝您新年快乐呀"),
            # ("z2546229681", "祝您新年快乐呀"),
            # ("snowmoon922", "祝您新年快乐呀"),
            # ("xiaozouchuanqi", "祝您新年快乐呀"),
            # ("邹宇宽", "祝您新年快乐呀"),
            # ("jzou0451", "祝您新年快乐呀"),
            # ("T15053356563", "祝您新年快乐呀"),
            # ("zyf_0407_16", "祝您新年快乐呀"),
            # ("yang7031223", "祝您新年快乐呀"),
            # ("zhouyou537452", "祝您新年快乐呀"),
            # ("jlq020506", "祝您新年快乐呀"),
            # ("Zihua3788", "祝您新年快乐呀"),
            # ("ya2505246934", "祝您新年快乐呀"),
            # ("Ryan20040319", "祝您新年快乐呀"),
            # ("Zhang15153233236", "祝您新年快乐呀"),
            # ("A1_77788999", "祝您新年快乐呀"),
            # ("z13156001150", "祝您新年快乐呀"),
            # ("Y_Z_D_02", "祝您新年快乐呀"),
            # ("YZH_1408Yu", "祝您新年快乐呀"),
            # ("lfkj5252", "祝您新年快乐呀"),
            # ("VY2401242311", "祝您新年快乐呀"),
            # ("Irene-zone", "祝您新年快乐呀"),
            # ("zhanx7953", "祝您新年快乐呀"),
            # ("ybc18678901251", "祝您新年快乐呀"),
            # ("yuanhe cui", "祝您新年快乐呀"),
            # ("As731408207", "祝您新年快乐呀"),
            # ("yjl530887025", "祝您新年快乐呀"),
            # ("angela411390908", "祝您新年快乐呀"),
            # ("闫玺昊", "祝您新年快乐呀"),
            # ("y396920969", "祝您新年快乐呀"),
            # ("yangzhen942966", "祝您新年快乐呀"),
            # ("xxxsssllnn", "祝您新年快乐呀"),
            # ("徐铭阳大一级软工", "祝您新年快乐呀"),
            # ("HeleneLi0323", "祝您新年快乐呀"),
            # ("JiyangEgbertXin", "祝您新年快乐呀"),
            # ("lan_ziziy", "祝您新年快乐呀"),
            # ("Haipengcrx", "祝您新年快乐呀"),
            # ("alexww666666", "祝您新年快乐呀"),
            # ("maomao538739", "祝您新年快乐呀"),
            # ("Achenblessed", "祝您新年快乐呀"),
            # ("小屁孩Brady", "祝您新年快乐呀"),
            # ("肖丽老师", "祝您新年快乐呀"),
            # ("Xiaobbbbbao", "祝您新年快乐呀"),
            # ("xiac605", "祝您新年快乐呀"),
            # ("DZ002625", "祝您新年快乐呀"),
            # ("wmy20100328", "祝您新年快乐呀"),
            # ("吴垒清", "祝您新年快乐呀"),
            # ("a12897007711", "祝您新年快乐呀"),
            # ("WillieScholtz", "祝您新年快乐呀"),
            # ("wfs", "祝您新年快乐呀"),
            # ("Qingdaoweihui", "祝您新年快乐呀"),
            # ("静心", "祝您新年快乐呀"),
            # ("Wry-QD-Gem", "祝您新年快乐呀"),
            # ("wojianwojia", "祝您新年快乐呀"),
            # ("wmm15066845826", "祝您新年快乐呀"),
            # ("Duncan Wang", "祝您新年快乐呀"),
            # ("yuan__1236", "祝您新年快乐呀"),
            # ("Johnwatson81", "祝您新年快乐呀"),
            # ("VINCEBOYY", "祝您新年快乐呀"),
            # ("Ny2003aa", "祝您新年快乐呀"),
            # ("Troy_0121", "祝您新年快乐呀"),
            # ("Trenteno", "祝您新年快乐呀"),
            # ("hyyahahahaha", "祝您新年快乐呀"),
            # ("Sxj_030124", "祝您新年快乐呀"),
            # ("wangn41", "祝您新年快乐呀"),
            # ("lwf00012349", "祝您新年快乐呀"),
            # ("YIYAN040131", "祝您新年快乐呀"),
            # ("TadoreM_0823", "祝您新年快乐呀"),
            #("drhou1974", "祝您新年快乐呀"),
            #("rkdtngus", "祝您新年快乐呀"),
            ("zhongzhengpinghe-", "祝您新年快乐呀"),
            ("AirJosuke25", "祝您新年快乐呀"),
            ("AI-12-88", "祝您新年快乐呀"),
            ("w1554985931", "祝您新年快乐呀"),
            ("sunyaxin_890929", "祝您新年快乐呀"),
            ("sophia 王孜玉", "祝您新年快乐呀"),
            ("bryexein", "祝您新年快乐呀"),
            ("Meiqiu_mao", "祝您新年快乐呀"),
            ("a915206565", "祝您新年快乐呀"),
            ("JSP_0377", "祝您新年快乐呀"),
            ("sds0817", "祝您新年快乐呀"),
            ("sheyue21844", "祝您新年快乐呀"),
            ("l1870255826", "祝您新年快乐呀"),
            ("yajishkabed", "祝您新年快乐呀"),
            ("chunsheng4862", "祝您新年快乐呀"),
            ("Ali-Fu-Chong", "祝您新年快乐呀"),
            ("深度技术维修店老大哥！", "祝您新年快乐呀"),
            ("Z132613577", "祝您新年快乐呀"),
            ("duanchichongsheng", "祝您新年快乐呀"),
            ("xiaochuanbisskobe", "祝您新年快乐呀"),
            ("yudongluan", "祝您新年快乐呀"),
            ("houzmiracle", "祝您新年快乐呀"),
            ("longxutang04", "祝您新年快乐呀"),
            ("S52_Hertz03", "祝您新年快乐呀"),
            ("gzh15225012244", "祝您新年快乐呀"),
            ("Rosieeeeee1998", "祝您新年快乐呀"),
            ("lzc041231_", "祝您新年快乐呀"),
            ("lfs20020219", "祝您新年快乐呀"),
            ("Onlooker_Ther", "祝您新年快乐呀"),
            ("QuinnLKL", "祝您新年快乐呀"),
            ("bb16yyyy", "祝您新年快乐呀"),
            ("WMXX1127", "祝您新年快乐呀"),
            ("phOenixNeverdiE", "祝您新年快乐呀"),
            ("pkr040", "祝您新年快乐呀"),
            ("LQNAIHF1122", "祝您新年快乐呀"),
            ("AAD25345", "祝您新年快乐呀"),
            ("nichoxo", "祝您新年快乐呀"),
            ("neo1997lee", "祝您新年快乐呀"),
            ("w1349912895", "祝您新年快乐呀"),
            ("ye66620", "祝您新年快乐呀"),
            ("Leila0923_", "祝您新年快乐呀"),
            ("MrDigiShark", "祝您新年快乐呀"),
            ("DJY18500137363", "祝您新年快乐呀"),
            ("sunruodong09", "祝您新年快乐呀"),
            ("Zhzj96", "祝您新年快乐呀"),
            ("x18660290378", "祝您新年快乐呀"),
            ("hutudebao8887", "祝您新年快乐呀"),
            ("mahxsecret", "祝您新年快乐呀"),
            ("YoungPhysid", "祝您新年快乐呀"),
            ("满江红", "祝您新年快乐呀"),
            ("吴瑞英", "祝您新年快乐呀"),
            ("fuyubo2004", "祝您新年快乐呀"),
            ("Akunmingyin", "祝您新年快乐呀"),
            ("hhh-hhh--h", "祝您新年快乐呀"),
            ("Jnw5802496h", "祝您新年快乐呀"),
            ("a15953284862", "祝您新年快乐呀"),
            ("hsu136153", "祝您新年快乐呀"),
            ("ggy13792498138", "祝您新年快乐呀"),
            ("日新科技", "祝您新年快乐呀"),
            ("il218121", "祝您新年快乐呀"),
            ("ThisIsLean", "祝您新年快乐呀"),
            ("linjun1300169", "祝您新年快乐呀"),
            ("linyunhai001", "祝您新年快乐呀"),
            ("ll_18804099711", "祝您新年快乐呀"),
            ("李海 老大哥", "祝您新年快乐呀"),
            ("Mynew_WeChatID", "祝您新年快乐呀"),
            ("LWbiocYN", "祝您新年快乐呀"),
            ("ll_ll_ld", "祝您新年快乐呀"),
            ("fuwuyou021", "祝您新年快乐呀"),
            ("Canada ", "祝您新年快乐呀"),
            ("nijiayi12345", "祝您新年快乐呀"),
            ("wyyyccco", "祝您新年快乐呀"),
            ("Leee111234", "祝您新年快乐呀"),
            ("HYX_7777_", "祝您新年快乐呀"),
            ("C249793279", "祝您新年快乐呀"),
            ("KMkmKM0812", "祝您新年快乐呀"),
            ("A2331xn", "祝您新年快乐呀"),
            ("ca20040426", "祝您新年快乐呀"),
            ("Kevin Yu", "祝您新年快乐呀"),
            ("liyekai31", "祝您新年快乐呀"),
            ("J_Xue1218", "祝您新年快乐呀"),
            ("JustinLinKK", "祝您新年快乐呀"),
            ("Joe", "祝您新年快乐呀"),
            ("Coolxiaoyu_c", "祝您新年快乐呀"),
            ("Jingyue", "祝您新年快乐呀"),
            ("jinchesheng", "祝您新年快乐呀"),
            ("新航道冀老师", "祝您新年快乐呀"),
            ("zouchunyang", "祝您新年快乐呀"),
            ("h2495990241", "祝您新年快乐呀"),
            ("shihehearz", "祝您新年快乐呀"),
            ("Jerry0509_", "祝您新年快乐呀"),
            ("zhangzhuduyi031106", "祝您新年快乐呀"),
            ("sunll1029", "祝您新年快乐呀"),
            ("LR20040513aa", "祝您新年快乐呀"),
            ("xhdzhujiao66", "祝您新年快乐呀"),
            ("荒野", "祝您新年快乐呀"),
            ("zhiqiang1929", "祝您新年快乐呀"),
            ("Hibik¡企业厨哦", "祝您新年快乐呀"),
            ("HenryH0827", "祝您新年快乐呀"),
            ("Haobo20140322", "祝您新年快乐呀"),
            ("s18554901882", "祝您新年快乐呀"),
            ("wendy531126893", "祝您新年快乐呀"),
            ("hezhidan86", "祝您新年快乐呀"),
            ("hjw13061370836", "祝您新年快乐呀"),
            ("hbjy8934", "祝您新年快乐呀"),
            ("YH0422-", "祝您新年快乐呀"),
            ("gxiaomeng16", "祝您新年快乐呀"),
            ("kyotyger", "祝您新年快乐呀"),
            ("wxxxxxy_2003", "祝您新年快乐呀"),
            ("jianlove_115946478", "祝您新年快乐呀"),
            ("Garyyy-P", "祝您新年快乐呀"),
            ("Jeremy21-MVB13-K24", "祝您新年快乐呀"),
            ("ilasierlfzbb", "祝您新年快乐呀"),
            ("whd17860932686", "祝您新年快乐呀"),
            ("FN_2100", "祝您新年快乐呀"),
            ("faz15666792826", "祝您新年快乐呀"),
            ("Drivingday1234", "祝您新年快乐呀"),
            ("Fares", "祝您新年快乐呀"),
            ("hamilton6868", "祝您新年快乐呀"),
            ("zyh1619931137", "祝您新年快乐呀"),
            ("ni1lli2cine", "祝您新年快乐呀"),
            ("Evelyn 郭老师好", "祝您新年快乐呀"),
            ("yuhang265347", "祝您新年快乐呀"),
            ("xzy777778961", "祝您新年快乐呀"),
            ("Jiangrunzhe2004", "祝您新年快乐呀"),
            ("fhjg474", "祝您新年快乐呀"),
            ("Elsiew1218", "祝您新年快乐呀"),
            ("e2745925", "祝您新年快乐呀"),
            ("zhuanzhedian8_7", "祝您新年快乐呀"),
            ("D13021670210", "祝您新年快乐呀"),
            ("dong12892", "祝您新年快乐呀"),
            ("WWGTTEOL", "祝您新年快乐呀"),
            ("MuxDestiny", "祝您新年快乐呀"),
            ("deandeanlee", "祝您新年快乐呀"),
            ("dubao2289044559", "祝您新年快乐呀"),
            ("hzy1452274770", "祝您新年快乐呀"),
            ("Crayon Shin-chan 代写", "祝您新年快乐呀"),
            ("coachshi", "祝您新年快乐呀"),
            ("C49784978", "祝您新年快乐呀"),
            ("DJYG00099", "祝您新年快乐呀"),
            ("春天里", "祝您新年快乐呀"),
            ("s-m-r-0113", "祝您新年快乐呀"),
            ("Iceland ", "祝您新年快乐呀"),
            ("fyx-flying", "祝您新年快乐呀"),
            ("cgq1213256416", "祝您新年快乐呀"),
            ("陈晨", "祝您新年快乐呀"),
            ("Pku1314520yyds", "祝您新年快乐呀"),
            ("Guilin2245", "祝您新年快乐呀"),
            ("璨若星辰", "祝您新年快乐呀"),
            ("CaCaCammmila", "祝您新年快乐呀"),
            ("hmcalder", "祝您新年快乐呀"),
            ("Joelxh99", "祝您新年快乐呀"),
            ("brantshi144", "祝您新年快乐呀"),
            ("Bob 高翔宇", "祝您新年快乐呀"),
            ("FairyNiuB", "祝您新年快乐呀"),
            ("zm130906i", "祝您新年快乐呀"),
            ("lxhixx_", "祝您新年快乐呀"),
            ("ArielZhouRealtor", "祝您新年快乐呀"),
            ("LKH25800", "祝您新年快乐呀"),
            ("Andrew", "祝您新年快乐呀"),
            ("Brujah4496", "祝您新年快乐呀"),
            ("Freshness_i", "祝您新年快乐呀"),
            ("Algebrast", "祝您新年快乐呀"),
            ("_13361201471", "祝您新年快乐呀"),
            ("abbbb5520", "祝您新年快乐呀"),
            ("cygj3666", "祝您新年快乐呀"),
            ("tiexuedanxin343862", "祝您新年快乐呀"),
            ("吴瑞启", "祝您新年快乐呀"),
            ("吴立清", "祝您新年快乐呀"),
            ("tianlangxing5", "祝您新年快乐呀"),
            ("qr15006432388", "祝您新年快乐呀"),
            ("Esther_juan", "祝您新年快乐呀"),
            ("x7198002o", "祝您新年快乐呀"),
            ("叔叔好！", "祝您新年快乐呀"),
            ("a36393038", "祝您新年快乐呀"),
            ("huan-chen-11", "祝您新年快乐呀"),
            ("qdwyz2003", "祝您新年快乐呀"),
            ("EMILY8大表姐", "祝您新年快乐呀"),
            ("伯long1913", "祝您新年快乐呀"),
            ("爸爸", "祝您新年快乐呀"),
            ("Annie", "祝您新年快乐呀"),
            ("matina 李诺仪", "祝您新年快乐呀")
        ]
        st_time = time.time()
        i = 0
        for user, message in contact_list:
            piece_of_trash.send_message(user, message)
            print("")
            end_time = time.time()
            delta = - st_time + end_time
            print(f"this garbage operation: {delta} ")
            print("this is",i,"th order")
            i = i + 1

class piece_of_trash:
    @staticmethod
    def send_message(user, message):
        try:
            piece_of_trash.find_friend(user)
            print("yes has been found")
            piece_of_trash.send_message_to_friend(message)

        except Exception as e:
            print(f"wtf is going on?: {e}")

    @staticmethod
    def open_wechat():
        pyautogui.hotkey('ctrl', 'alt', 'w')
        time.sleep(1)

    @staticmethod
    def find_friend(user_name):
        pyautogui.hotkey('ctrl', 'f')
        pyperclip.copy(user_name)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.press('enter')

    @staticmethod
    def send_message_to_friend(message):
        time.sleep(5)
        pyperclip.copy(message)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(10)
        pyautogui.press('enter')
        time.sleep(3)

    @staticmethod
    def close_wechat():
        pyautogui.hotkey('ctrl', 'alt', 'w')

if __name__ == "__main__":
    piece_of_trash.open_wechat()
    This_is_shxtbox.main()
    piece_of_trash.close_wechat()
