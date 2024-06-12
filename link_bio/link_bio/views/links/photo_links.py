import reflex as rx

def len_photos(sub: str) -> int:
    if sub == "TBM3":
        return len(TBM3)
    elif sub == "C202":
        return len(C202)
    elif sub == "D520":
        return len(D520)
    elif sub == "SPAD":
        return len(SPAD)
    else:
        return 0

# This file contains the links to the photos of the models
TBM3 = [f"https://i.imgur.com/Zueckgk.jpeg",f"https://i.imgur.com/GXGqGCV.jpeg",
        f"https://i.imgur.com/9KWGtVw.jpeg",f"https://i.imgur.com/byCJrF5.jpeg",f"https://i.imgur.com/8DaQK4v.jpeg",
        f"https://i.imgur.com/RcvJZLN.jpeg",f"https://i.imgur.com/buNYhgh.jpeg",f"https://i.imgur.com/GrwEFgq.jpeg",
        f"https://i.imgur.com/S350cNQ.jpeg",f"https://i.imgur.com/Qjey7G1.jpeg",f"https://i.imgur.com/wCwPRmz.jpeg",
        f"https://i.imgur.com/ZAXaQ2U.jpeg",f"https://i.imgur.com/NnvIxkZ.jpeg",f"https://i.imgur.com/CffgnbP.jpeg",
        f"https://i.imgur.com/bzUXHNC.jpeg",f"https://i.imgur.com/smC4URy.jpeg",f"https://i.imgur.com/z1Rbdzz.jpeg",
        f"https://i.imgur.com/8WNZ0dh.jpeg",f"https://i.imgur.com/IMpVAkQ.jpeg",f"https://i.imgur.com/9QD5Kq6.jpeg",
        f"https://i.imgur.com/MDCe6F3.jpeg",f"https://i.imgur.com/i6bOSvf.jpeg",f"https://i.imgur.com/kX0UaGc.jpeg",
        f"https://i.imgur.com/wL7zoUn.jpeg",f"https://i.imgur.com/MWP4SZ7.jpeg",f"https://i.imgur.com/JLZTT2r.jpeg",
        f"https://i.imgur.com/R1wrgRP.jpeg",f"https://i.imgur.com/lLxP257.jpeg",f"https://i.imgur.com/iHNb3qw.jpeg",
        f"https://i.imgur.com/zmLz8wr.jpeg",f"https://i.imgur.com/NSNhUH1.jpeg",f"https://i.imgur.com/jWWn6kY.jpeg",
        f"https://i.imgur.com/DKq3BCl.jpeg",f"https://i.imgur.com/SnS1hr1.jpeg",f"https://i.imgur.com/WeQ05eO.jpeg",
        f"https://i.imgur.com/jPA41Is.jpeg",f"https://i.imgur.com/H1LAiUY.jpeg",f"https://i.imgur.com/aLW8Etn.jpeg",
        f"https://i.imgur.com/vGbOrkE.jpeg",f"https://i.imgur.com/RllEzIm.jpeg",f"https://i.imgur.com/hFeTb8Z.jpeg",
        f"https://i.imgur.com/esCeiuF.jpeg",f"https://i.imgur.com/avnVSxt.jpeg",f"https://i.imgur.com/oV0myCz.jpeg"]
C202 = [f"https://i.imgur.com/tWiwJC3.jpeg",f"https://i.imgur.com/sLuApk2.jpeg",f"https://i.imgur.com/wEKgTUu.jpeg",
        f"https://i.imgur.com/fi4cfmm.jpeg",f"https://i.imgur.com/dPVHkF1.jpeg",f"https://i.imgur.com/sNEALo6.jpeg",
        f"https://i.imgur.com/oUJm445.jpeg",f"https://i.imgur.com/4pS1VuA.jpeg",f"https://i.imgur.com/UWCBcRI.jpeg",
        f"https://i.imgur.com/mjXQfo9.jpeg",f"https://i.imgur.com/PwPGLwj.jpeg",f"https://i.imgur.com/Q33A0Hx.jpeg",
        f"https://i.imgur.com/aiIMRJQ.jpeg",f"https://i.imgur.com/V60pSmE.jpeg",f"https://i.imgur.com/toDDyvQ.jpeg",
        f"https://i.imgur.com/BosYlJK.jpeg",f"https://i.imgur.com/330PlEY.jpeg",f"https://i.imgur.com/4UJSvH5.jpeg",
        f"https://i.imgur.com/biCQnww.jpeg",f"https://i.imgur.com/uNL65Rm.jpeg",f"https://i.imgur.com/XUC6MOl.jpeg",
        f"https://i.imgur.com/hIuWqh4.jpeg",f"https://i.imgur.com/BPzBf9N.jpeg",f"https://i.imgur.com/DUto2fD.jpeg",
        f"https://i.imgur.com/mIS47sS.jpeg",f"https://i.imgur.com/RjWbDnD.jpeg",f"https://i.imgur.com/uhWSCxt.jpeg",
        f"https://i.imgur.com/KKDUiGk.jpeg",f"https://i.imgur.com/XlLA3Ou.jpeg",f"https://i.imgur.com/8l5kwq6.jpeg",
        f"https://i.imgur.com/IPWVrTU.jpeg",f"https://i.imgur.com/7APloDH.jpeg",f"https://i.imgur.com/vXRGEhf.jpeg",
        f"https://i.imgur.com/u2Byvk9.jpeg",f"https://i.imgur.com/lWZ2N0s.jpeg",f"https://i.imgur.com/Ay0XATD.jpeg",
        f"https://i.imgur.com/KZhJOL8.jpeg"]
D520 = [f"https://i.imgur.com/F06jQ1A.jpeg",f"https://i.imgur.com/fBsJ2XO.jpeg",f"https://i.imgur.com/lFVCZyH.jpeg",
        f"https://i.imgur.com/NyfBthm.jpeg",f"https://i.imgur.com/l1fS10j.jpeg",f"https://i.imgur.com/g0kfLtr.jpeg",
        f"https://i.imgur.com/LMp5uyd.jpeg",f"https://i.imgur.com/7PeoWcY.jpeg",f"https://i.imgur.com/vemJ6Ji.jpeg",
        f"https://i.imgur.com/xzOoxsT.jpeg",f"https://i.imgur.com/KocNPXF.jpeg",f"https://i.imgur.com/vyiiQ3h.jpeg",
        f"https://i.imgur.com/NrouCzJ.jpeg",f"https://i.imgur.com/h38J7aR.jpeg",f"https://i.imgur.com/JyHMSZW.jpeg",
        f"https://i.imgur.com/0sxyHX3.jpeg",f"https://i.imgur.com/iwle3RT.jpeg",f"https://i.imgur.com/ptkPmD7.jpeg",
        f"https://i.imgur.com/SxKz0Vl.jpeg",f"https://i.imgur.com/6kACxqw.jpeg",f"https://i.imgur.com/GonIk7o.jpeg",
        f"https://i.imgur.com/BQEGiWi.jpeg",f"https://i.imgur.com/MZyaHqw.jpeg",f"https://i.imgur.com/NjS9eA9.jpeg",
        f"https://i.imgur.com/S1Bbpd5.jpeg",f"https://i.imgur.com/g7dOXHp.jpeg",f"https://i.imgur.com/MLTOyZo.jpeg",
        f"https://i.imgur.com/1Y6fB2v.jpeg",f"https://i.imgur.com/9TZfUQP.jpeg",f"https://i.imgur.com/twegKI6.jpeg",
        f"https://i.imgur.com/H97Cvwi.jpeg",f"https://i.imgur.com/eqf80mg.jpeg",f"https://i.imgur.com/cKcNrzK.jpeg",
        f"https://i.imgur.com/0XgJJWy.jpeg",f"https://i.imgur.com/tVxj5rX.jpeg",f"https://i.imgur.com/HM6ALHv.jpeg",
        f"https://i.imgur.com/DmZ6ZJz.jpeg",f"https://i.imgur.com/GKJhzMn.jpeg",f"https://i.imgur.com/RfQxVXj.jpeg",
        f"https://i.imgur.com/4PSdCbM.jpeg",f"https://i.imgur.com/tAU8zo9.jpeg",f"https://i.imgur.com/5STLHFD.jpeg",
        f"https://i.imgur.com/Kx4NBUM.jpeg",f"https://i.imgur.com/hPiAYRj.jpeg",f"https://i.imgur.com/M3QOXEy.jpeg",
        f"https://i.imgur.com/Y7spGuH.jpeg",f"https://i.imgur.com/KTW9gYh.jpeg"]
SPAD = [f"https://i.imgur.com/vFH02JW.jpeg",f"https://i.imgur.com/DcUc8ng.jpeg",f"https://i.imgur.com/AesWqxg.jpeg",
        f"https://i.imgur.com/VpOlnnX.jpeg",f"https://i.imgur.com/s4ARGvP.jpeg",f"https://i.imgur.com/AbpwlS1.jpeg",
        f"https://i.imgur.com/IOqjisK.jpeg",f"https://i.imgur.com/bDTBSVd.jpeg",f"https://i.imgur.com/f7Nnanw.jpeg",
        f"https://i.imgur.com/r167c4E.jpeg",f"https://i.imgur.com/4qxy812.jpeg",f"https://i.imgur.com/dxwPG88.jpeg",
        f"https://i.imgur.com/EDDhZsz.jpeg",f"https://i.imgur.com/n4Pgf5q.jpeg",f"https://i.imgur.com/8PrP4nr.jpeg",
        f"https://i.imgur.com/xJJNIbW.jpeg",f"https://i.imgur.com/hAJdXzx.jpeg",f"https://i.imgur.com/jmdgJC4.jpeg",
        f"https://i.imgur.com/xvhcKo4.jpeg",f"https://i.imgur.com/IHSOgbW.jpeg",f"https://i.imgur.com/rWhFvGC.jpeg",
        f"https://i.imgur.com/iopvcOI.jpeg",f"https://i.imgur.com/i7IjB2w.jpeg",f"https://i.imgur.com/IVBQrdN.jpeg",
        f"https://i.imgur.com/GH1BF9x.jpeg",f"https://i.imgur.com/M3eHDnh.jpeg",f"https://i.imgur.com/HWrFWMU.jpeg",
        f"https://i.imgur.com/m7WB0Bb.jpeg",f"https://i.imgur.com/mriXPQq.jpeg",f"https://i.imgur.com/IUsIvz9.jpeg"]

