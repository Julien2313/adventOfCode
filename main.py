#http://adventofcode.com/2017/
import sys

DAY7INPUT = """wdysq (135) -> sxldvex, wiasj
vjwuuft (33) -> inuci, neddz, rwamq
oislgqy (77)
lphki (233)
wgbviwb (417)
vikip (136) -> eofyk, dkexo, xzsxx
elmieqh (19) -> dbziu, spefs, krtxpw
tmzef (79)
ectlgy (232) -> zmstcy, ncobxr
sdatyo (91)
uisri (11)
smqimxg (132) -> husor, olzys
pltzthr (82)
szaqj (188) -> ptnndxj, fljpye
jqdngi (58)
uazwsu (15)
xrrhso (79)
gxeehd (68) -> iweii, rnqlzmv, hpmtom, vfzwqfr, xfzxrd, sgqhelx, hibjkps
evkoenr (43) -> oecxbyt, qbthgst
qivuzn (52)
udeev (389) -> lphki, qthzk, hpgsb
izgqzs (96) -> vbxzk, ubrrdtd
naxtp (65)
mvtkwn (42)
sxldvex (34)
tnlpmw (49)
rzbrbmy (31) -> dvnqv, helyy
esavxwq (81)
yqgru (465) -> gfuyuz, elmieqh, xckzut, tmbhjxf
ygypj (1303) -> ohcuki, ejdjxu, ytabct
yggqq (855) -> gowlaq, ebtoxi, xpljwl
ubaxya (92)
pjkzokv (23)
lvarp (76)
yrysmsi (14)
nofepy (23)
apjeywv (132) -> kclmmu, exsugls
licrtwb (56)
gspffet (84) -> wqzxa, lptaikg
gkrqba (82)
mqreb (126) -> jvdoo, paykww
xtidu (12)
kjauagn (88)
vvafqjs (56) -> qbvhefh, vfhgfb, iqtyv, ebdva, uxqkau, tydtcxc
snuewn (118024) -> vvafqjs, mhaucon, kikva, mqnbmre
gtkii (163) -> txcon, vuvwa
oaoisa (61)
ssqrs (24)
ybditq (21)
xgqxofa (119) -> bedzc, hdbkw, zwgsh
wxfir (71)
pxvse (19)
xemcuk (23)
paunv (28) -> zzvhmse, mubkcmk, vksephm, cbsdget, mellhhn
couhjsv (11)
tuzpls (58)
puomwl (90) -> wtxjnc, jdjbnc
wudlze (78)
ibslyw (153) -> ksncpee, npvuz
zzmczwl (54)
kidvt (3136) -> tuzzzct, qtqhwon
patlvg (20)
yvvxtg (90)
epxwjhy (22)
epvyxld (17)
xhecnbf (85) -> yituewe, wwhyd
mqsrwsz (26)
bhyzi (73)
batky (18815) -> woctu, iykjtnw, tpiwftj
sdponx (44)
qhotyqx (95) -> vdwfz, agthd, tuwedv, ixkkdyc, lnlkwq, bvmhqar, rlwmfp
nubqteb (89)
zygfdu (70)
tkerz (18)
solqvvf (10)
akiaxs (86)
jsfqyd (70)
aialff (68)
uiilkiq (73)
adlyhbs (46)
tnljdhr (20)
frctm (471) -> isqnx, euhgw, nrfqc, cmmnjch, zevrg
jjklma (105) -> xrrhso, uyjor
lpmnwh (56) -> orrfh, bqfzqra
owxski (23)
gqxyh (18)
lpyntz (91)
ivvyjos (81)
qssjswr (268)
jkbks (225)
jwbdb (83)
axqrke (119) -> mgoic, yivgs, bxggi, xamfjfv
uwizlce (24)
wuwhup (50)
suawycj (60)
wazvn (99)
wtxjnc (53)
ebtoxi (64) -> ttbns, voxychz, umsdpa, ajjmsnw
uuhoydu (82) -> gvucdh, hesyq, glwsf
tshyvej (1373) -> ebiovn, uvzpp, pblqb
bhakbq (991) -> izqxal, nhhytw, flmma, isgky, coqek
hcsjun (60) -> inelfwo, qcnstq, eymmhh, lpyntz
otjbn (67) -> szaqj, kkhlzm, jtzdqn
vtwud (10735) -> jldhlug, ikfzj, tsevkec
heztht (86)
rqonynk (65) -> olzqxap, oyhqsok
esbdjah (61)
hdinwud (1515) -> bdiftdg, ydtuje, aambg
rbbjcq (71)
kimffjc (155)
wifrwut (91)
hrlgs (9)
ieowdj (76)
vpqsjbj (147) -> eziosif, rptcpf
rlurjca (51) -> gtbjtpi, ohpkkhx, zkwnhn, cagvlf, zvlobk, ahsqaob, iactix
yzykfd (43) -> atqfhm, kazwz
kikva (6131) -> gkpalaj, jafrv, uekzf
lsoen (51)
uexqjw (10923) -> dxczurt, omqhf, ylfxp, qofsaux
nlnphv (117) -> vzlzrt, ypiwnt
bemxocu (78)
etcsuuv (312)
ihwbmt (27)
oorvvpt (63)
dvnqv (88)
ntlawn (60)
jhaow (45)
kccpv (17)
kbybvzk (89)
ctcmfv (49)
ujqjrz (89)
xekft (62)
wihtv (1278) -> qgbbhdv, adlyhbs
agthd (158) -> ucnehpw, hnutx
vuytzn (21)
svcqds (7)
emqqf (5)
uqddsal (17) -> trait, sdatyo
uhwlk (252) -> sxtto, qyvsaxn
ttbgzv (46) -> rokri, pygoqsv
oecxbyt (71)
xunvu (33)
mvbtomp (35)
uxqkau (693) -> qubhi, gneut, htmcpcy, qmncyu, wdysq
ycrnaf (177) -> ssqrs, twimkx
nlalji (28)
dgvvo (37)
niydqsy (33)
pprvv (89)
tmbhjxf (135) -> jutep, vkhiz
iaftm (63)
zjnrzph (81) -> gsxmqnw, gnxfwv
ggzqccl (5)
wwtiby (121) -> kytha, dgzywn
zismp (58)
hjbrfba (28)
xnlkkx (79) -> puomwl, xnbvupf, hgksz
bptaz (38)
ozaogat (15)
hxxml (27) -> emazu, kproiw
xpptslq (76)
ilohfvn (10)
hadddf (128) -> geapi, ocltuv
gtprqg (17)
qofsaux (209) -> bbnjml, fwskxq
xpljwl (128) -> ufust, aialff
thhbhrm (41) -> smqkli, ovtfd
xamfjfv (36)
jdjbnc (53)
kecpcmj (72)
ixkkdyc (80) -> wutzrk, antev
ysnbr (35)
cyvwwa (190) -> jtqxxa, pgmtcg, btvsj
uyjor (79)
oztxmy (76)
cancxr (213) -> ivdvlvq, ykxalh
zlads (14)
peokkb (167) -> mqkqtjo, qpchzkg, epssvr, yzose
iauxpc (81)
qbodszw (945) -> rgdvqu, oktgjb, abstvp
dmwutl (73) -> desuqj, etjwno
fcaht (134) -> ajidd, kigxtt
fkgkcwd (51) -> mqwagy, gvtve, djvbdm, ckapp, ldiqm, ezspaq, pyrvg
dqzkic (1032) -> inglhm, dgxdydd, hxhhhu
ydtykm (75)
zatfy (35)
rmenjck (89)
nrfqc (238) -> zgxjjm, fwide
schexn (97)
lrplxk (22)
nroecsv (44)
kiawm (64)
zpfuxux (73)
mvdkbch (28)
sufdte (71) -> gfjeud, rbbjcq
xmjunhp (45)
wsnsqx (7)
etyaxa (13)
cfrqn (57)
tslujme (60)
bebuqpx (33)
wwyuud (11)
gtotarq (95)
vtopekt (65)
hxhhhu (230)
aubvpzf (73)
kllsasv (73) -> enuvuv, jlhipos, hittl, smyzyqg
mgiuz (94)
dsytvn (296) -> mxfonyo, yihru
icsxziz (256)
agflbq (73)
amtrbok (12)
qcebc (20)
eymmhh (91)
pbpva (95)
rodxm (199) -> rzvlc, vnmml, rrmlgct
ekblpi (97) -> flwbwcq, ecwpa, usgpgi, pknsw, gkjwl, zzfom
ltpmtif (86)
bkfnip (4873) -> murnoa, qhzem, udeev
yhiab (249) -> sdponx, yvattv
hbaai (70) -> rmnkup, dgtsic
anazjn (225)
zjjyjj (101) -> viwez, ihwbmt, qnwwjwt
husly (98)
jlhipos (20)
xflsc (2516) -> qodow, vdkhvyp, masvpfj
cenqs (156) -> jhaow, mivmhi
rgrcla (84) -> nroecsv, pexfst
pdddwgk (30)
upefkx (75)
abstvp (46) -> wqgoxl, gbwaobo
glzmsn (93)
bgtzw (37)
flvrfdl (146) -> ybditq, vuytzn, yqdaz
jmzpxql (47)
wulvcf (89)
mxfonyo (20)
aambg (69)
jfjvw (32)
uslhk (8)
wwzjdv (45)
zwtsg (248) -> bjjtifj, ogbov
mbxyf (56)
xckzut (157) -> gaalz, upefkx
trseebo (18)
hbcpm (32)
ggoaczz (88)
zangrh (66)
ktbto (55) -> pdqzfg, mfoismz, mkirruz
rhpcgg (197) -> evkoenr, klpzhup, cigew
kbbcau (25)
porttu (92) -> haaqbj, lttlp
gfsgzni (73)
pyaqqhu (134) -> kdkobz, szvocp
eiyiuq (54)
fjgjfpc (17)
lvvkjx (56)
kinah (22)
ivdvlvq (31)
njerlzh (35)
zzdae (63)
rrkbjhn (78)
hnutx (50)
oqokji (198)
voxychz (50)
zovlqz (56)
ulood (81)
yzttfu (15)
htmcpcy (203)
jmytuxi (221) -> dvuctqv, sgilmx, fqdolnu, rdrncg
rehhbv (17)
ixkpaf (59) -> jqbdh, atvtit, qcebc
antev (89)
jfikdf (20)
ykxalh (31)
vqwclk (19) -> ewldimp, wkeqlvj, ouxuh
hxeqn (528) -> kimffjc, qpgphk, vqfiq
umsdpa (50)
aodfzpi (69)
wutzrk (89)
jyjvpeb (81)
ttbns (50)
wmewl (977) -> yhiab, iordzi, uuhoydu
ydejjeb (159) -> yvcanc, jrrubn
bykuuwe (80)
iesjhoq (336) -> bhzfx, sxexfai, mjounwc
kdrhj (1832) -> rrkbjhn, gzpgvqq
smyzyqg (20)
kigxtt (80)
rokvo (7)
wpcng (50)
koevsvb (97)
yihru (20)
krtglj (18)
cmfwwv (40)
jsaujq (1397) -> rgrcla, vqwclk, rxilrp
gmjxxi (97)
ekvmhd (49)
lttlp (66)
takbkro (200) -> ngjipr, inhfutj
whvpgmw (54)
lqaveh (97)
qthzk (187) -> wntmkg, pjkzokv
haaqbj (66)
vxufrto (40)
zseldo (181) -> hdvtd, papbxya
psmgm (95)
clwtgt (34)
bpwxvvw (89)
pmyrysb (77)
gjclsl (75)
olzys (57)
woqoljk (99)
ocodtdz (30) -> gjclsl, ogioyhi
nbybi (54)
veiaf (139) -> vlqqgb, iaftm
uvzpp (165) -> mxvba, jjtafg
qodow (63) -> oqxnfd, rpxaf, sybnvtp
kouye (58)
dlhuell (84) -> schexn, otzinx
nlrlj (145) -> veknoj, lfpjfv, yrlnu, ugelox
sambc (138) -> mnoinr, pkordz
bypqww (50)
rgkfzk (35)
kiatxq (1232) -> dispgy, irnjtjo, iqpoc
gigtu (60)
xzsrv (89)
dhafpel (636) -> vxddev, nxkpnt, zbuftv
bqfzqra (71)
rcbqqok (243) -> ofrogun, wwyuud
oaqkk (69)
dgxdydd (132) -> mudewqe, bazwto
vxddev (128) -> bzpjiss, qmjamoi
iqtyv (800) -> lvtotof, zddmrx, yzykfd, nlnphv
vdcmrrr (93) -> xuoyxmc, amrcopl, fcnsfy
jutep (86)
cyanr (23)
cxyxa (97)
tuzkv (153) -> iflll, tipewrj
cdegn (52)
mvijo (35)
xnbvupf (60) -> frlgjzf, wtorpp
rwopuzo (15)
uxfsb (76)
qedyqs (157) -> bjzbqzq, alfqryh
rwhgw (76)
csmjozb (79) -> sasym, wmewl, kdrhj, btvmyff, sqkfgo, jcputh
jbujmr (294)
xvjfw (8)
ekfwu (17)
ebiovn (225) -> mnufo, rokvo
ohcuki (197) -> alsfpfg, xsfryrh
zavisuv (15)
glwsf (85)
vurdlqx (196) -> acfdkr, aefjv
ihksnmq (95)
ecwpa (248) -> soyta, ytomr
jldhlug (234)
oazfz (61)
rdrncg (16)
rrrmaka (51)
qhgzopn (66) -> tmzef, iiiupn
ifetn (86)
plgjg (99)
okjds (73)
algkwbg (99)
ugmhzm (56)
vvnhm (135) -> ntrtfv, ihuqmbd
csuywzh (1788) -> wgvpotf, fwtxvo, vikip, bpzhj, bomuft, otjbn, zsotrv
pawpvkj (47)
zzvkwsb (148) -> hjfucl, gxcft
aivbhtz (78)
nyckm (23)
qwqpht (68)
kbuurtb (62)
ahexrp (19)
dlikiv (247) -> kinah, sthtydb
udiai (50)
lopnwz (91)
xbtvux (73)
gvtve (222) -> typbqmw, vdsaccd, sdlta, uisri
vczyhcg (8)
edswttn (58)
kqaua (89)
lmnuii (536) -> rlwoz, gjvmrh, ukapl, lthoz, boahhv, ylpxahm, rqonynk
kwlyw (193) -> hcruo, kecpcmj
trskdr (322) -> hdrfo, bimxf
clbmn (33)
scffzsr (48)
ewldimp (51)
qhixu (21) -> roorbg, oruhqn, psmgm
ypcup (94)
vrszijz (56)
vksephm (157) -> ngkax, tkerz
sxtto (30)
tkojiz (12)
elygt (569) -> bixtvg, xsqbapj, ocodtdz
vdctvf (84) -> iauxpc, cuyweja
rktxkyb (108) -> xjbot, flwjj
zckdwxe (54)
vfzwqfr (54) -> mphzxio, clbmn, donnc, niydqsy
iqpoc (260) -> zlads, jhapr
pojst (51)
ueitm (169) -> emqqf, qqstwmn
dgzywn (39)
ldcmzd (130) -> mertvs, ggoaczz
xtgmmc (306)
mjounwc (9)
ftbiwxy (62)
ogioyhi (75)
fkitgnx (69)
gvucdh (85)
opsrep (43)
olsycb (59)
jiizacd (49)
qbthgst (71)
nxqvwm (69)
rvrzp (113) -> xrqhewm, ifetn
pkordz (84)
vempqu (6)
ulmwqtm (230)
zwgsh (43)
srgob (561) -> plrig, djbtbrk
rmnkup (47)
btvmyff (1442) -> mrqtrkq, zjjyjj, uqkskjn
nrfyua (11)
nuozixg (1064) -> nnelc, zmzobfp, oggljxs
icrvj (22)
vksphlf (1423) -> kdykksn, wwtiby, uqddsal
xmnbar (58)
ukapl (195)
lijszmh (44)
zzonk (28)
jhapr (14)
mrqtrkq (88) -> zaxbfog, pawpvkj
aibtig (109) -> ggzqccl, hyxtojc
vuvwa (87)
ahysv (90)
mqwagy (88) -> uxlisdh, rmenjck
xpttnwd (95)
oullg (25) -> dlhuell, imrwgqw, hadddf, rktxkyb, zwtsg, wllrov
bwsgfa (22)
vmiykci (153)
jcgvp (18) -> mvbtomp, zatfy
wetluzb (33)
zvnzrr (37)
sgilmx (16)
geabygu (96)
kakvi (41)
fuujiy (92) -> xnfuz, urrhqwc, fmdfm
ppvsy (285)
nyuxiu (122) -> nzvqjrt, dhzsao
tjwynpa (75)
gowlaq (138) -> uwvfga, bnvlydl
snywwu (26) -> snqey, aodfzpi
cvude (41)
snqey (69)
ejqam (17)
pgmtcg (47)
rtcqml (85) -> zangrh, dspug
ezspaq (215) -> rehhbv, epvyxld, oguxu
ytabct (89) -> frfotet, zerxp
nxkpnt (248)
qubhi (107) -> lnznpq, scffzsr
tfotbwz (424)
wkgyfpp (824) -> ccbie, iesjhoq, kdffrsb
wjsxcmb (95)
ztdbvxb (53) -> zismp, dqoagdt, yxfjglq, givaxj
ouxuh (51)
xfzxrd (22) -> kakvi, mjlvx, wridnv, zeexkde
rekerpj (7)
redkli (81)
qdkhjb (53)
yituewe (95)
ocnkhq (10)
iaayhc (300) -> fwhhoz, ycrnaf, jkbks, anazjn, yhzjjgc, pocwgw
mjlzzq (212) -> hwycny, gmzabjk
rhaoo (36) -> kdzhiq, ydkhmp, dsytvn, wzezz
fqkzcq (293) -> gztng, oiaxzp
essijo (1248) -> wuqapgg, msmxf
ckapp (94) -> clktah, akiaxs
nktwwvp (159) -> qivuzn, cdegn
qxwdzl (50)
lfpjfv (48)
lmfclbd (14)
cglyptu (240) -> icrvj, epxwjhy, tpmqmg
dhzsao (24)
bckfa (16) -> ntlawn, tslujme, ccjze, woklobt
mivmhi (45)
bfjxeyo (24)
plrig (53)
ijlooi (1429) -> jcgvp, zvsgd, fzafkj
pyhcj (64)
gdvbtjk (71)
fxrkz (70)
husor (57)
riiaj (44) -> lvvkjx, mbxyf
lxmvg (4738) -> msjbv, ijoaqyv, yname
wntmkg (23)
helyy (88)
muxvdx (57) -> veiaf, rcbqqok, gfnmx, zezeds, ktbto, qedyqs
rroub (41)
hnwfe (89)
enuvuv (20)
wzzlsg (18)
hpgsb (81) -> xpptslq, jtoryw
woklobt (60)
jicyq (18)
lybwr (64)
ujgpnsy (12)
mbtweib (86)
vgzejbd (10) -> vuoqao, vwkkml, kmpfxl, snuewn, jjgjvki, fiprusz
vgfveov (198)
lvtotof (49) -> pprvv, gsckda
ylpxahm (33) -> jyjvpeb, tytsynv
glximrw (53)
iykjtnw (542) -> dizqtw, oiozpzq, dmwutl
xuoyxmc (51)
wpvale (18626) -> wihtv, isbdm, gxeehd
jruttt (28)
urrhqwc (84)
yfyaho (7)
klpzhup (11) -> befwz, mypula, xmnbar
kclmmu (49)
qcnstq (91)
sasym (13) -> vimnt, eoign, lusub, peokkb, mlhaxv
mgoxhns (130) -> edswttn, ioycu
stzzli (89)
ltesfzf (44) -> sufdte, vpqsjbj, oghyxz, hxxml, mnhrjdv
yxfjglq (58)
fuhbay (82)
gxcft (25)
rwamq (86)
qxqwmye (68)
ketopn (42)
tmsmb (84) -> pkxrm, pbbkg
zerxp (75)
zpbrw (95)
wuqapgg (66)
nmsats (82)
vvzctek (9)
cmoty (91)
qkkhj (88)
pocct (99)
xyfvxng (45)
mqnbmre (2069) -> vecnb, azhddw, muxvdx, qbodszw, yggqq
msjbv (918) -> nktwwvp, qijleb, ttnoqm, ulaio, furlcyu
mkirruz (70)
mubkcmk (163) -> solqvvf, ocnkhq, wntitz
lvzzwy (89)
ypiwnt (55)
bveilrx (306) -> pxvse, ahexrp
shiaqps (45)
mlhaxv (297) -> ctcmfv, ekvmhd
eiohuhm (72)
isqnx (122) -> azgohsw, pltzthr
qqstwmn (5)
fiwvclv (80)
zobti (87)
qbvhefh (53) -> ylazd, cyvwwa, sfkpzr, zsjlevq, zseldo
xqgxel (54)
yrlnu (48)
rrmlgct (19)
jtzdqn (178) -> lsoen, pojst
nffvt (37)
axtepsa (13)
ngkax (18)
viwez (27)
kdykksn (7) -> geabygu, cfiqn
zvlobk (419) -> mdfkbxa, wzzlsg
xsqbapj (164) -> xqxvktz, xvjfw
nzvqjrt (24)
gbqbg (18)
hskko (38)
bgmntpq (6)
zddmrx (227)
dgtsic (47)
iijfq (73)
qytxu (71)
mklcsj (54)
jnwdraz (63) -> aubvpzf, zpfuxux
hudde (1072) -> wyrfplr, rzbrbmy, ujmfmiu
jcoyk (18)
dspug (66)
qgbbhdv (46)
neddz (86)
boahhv (195)
ajjmsnw (50)
lusub (209) -> nrloleu, lfwpqb
bkgise (17)
xsgyar (568) -> fesce, vfteg, thhbhrm, vvnhm
mudewqe (49)
trait (91)
fljpye (46)
xobszr (61)
pkxrm (57)
qrynkpt (22) -> kswafh, oztxmy, zejcp
frlgjzf (68)
aomksx (70) -> pmyrysb, robpw
gjvmrh (167) -> xxtyban, mfjdb
atvtit (20)
ihuqmbd (34)
mfjdb (14)
rptcpf (33)
ljitswv (89)
zkujvlv (51)
ydtuje (69)
emazu (93)
sqkfgo (1451) -> ueitm, okbtg, cnzynyj
flmma (86) -> ygglox, ocvrlia
jnqgs (76)
ctken (72)
kxdbyp (20)
ktlkx (112) -> etyaxa, axygpr, rqsyc, axtepsa
hesyq (85)
tydtcxc (919) -> swcsd, nkclzqq, dhcopz
sqbxzl (12)
dispgy (52) -> olsycb, ynecxzo, esqvkcm, xclsj
djbtbrk (53)
svjnd (47)
fizbyu (78)
vqfiq (61) -> zdrhuz, jmzpxql
tqsrg (70)
dulrvcq (2086) -> apjeywv, vurdlqx, bwemy, ulmwqtm, qkxtwct
gfjeud (71)
xdzgwl (220) -> jicyq, prbbfe
jcputh (196) -> xdzgwl, rodxm, piutfin, ezmot, bckfa, zyisjsj, icsxziz
gbwaobo (94)
mlyar (44)
zsotrv (751) -> wudlze, hjmreq
chxgqe (47)
junva (83)
fmdfm (84)
ewwab (70)
hdrfo (51)
qijleb (111) -> qngug, voxemk
qmjamoi (60)
pyrvg (230) -> shcavm, trseebo
joszidy (95)
rxilrp (138) -> gtprqg, xqgqp
ptnndxj (46)
typbqmw (11)
fesce (39) -> fuhbay, jozav
oeixw (65)
gjhfseh (20)
zeexkde (41)
ynecxzo (59)
oqfpo (78)
keazynv (68)
gnsdn (51) -> njerlzh, rgkfzk, lhyzwtf
sqljeh (20)
dclmckh (93)
rqsyc (13)
wvwjep (70)
ncobxr (8)
builgr (78)
xkdjbxo (81)
bzpjiss (60)
vfomix (95)
wtorpp (68)
pruui (1276) -> glaosn, xgqxofa, ggkael
monhu (76)
piutfin (156) -> wpcng, qxwdzl
wrwim (10)
jrrubn (52)
vkdytw (24)
vdtdmy (26)
pbbkg (57)
uwviodb (208) -> bkxfso, evrtfzj
vfhgfb (1084) -> gnsdn, ttbgzv, pyaqqhu, riiaj
iordzi (223) -> cfrqn, nzuhp
biffdx (42)
bpsesr (50)
cglfuq (199) -> vempqu, noogeuk, bgmntpq
bkxfso (19)
oopnu (88)
wlavb (92)
gmzabjk (41)
ehrfv (57) -> pruui, eondv, ygypj, vksphlf
lpwuzn (89)
cnzynyj (89) -> wwzjdv, xyfvxng
dgmtgrv (12)
hpmtom (50) -> zzpwgcd, qxqwmye
jafrv (719) -> qhgzopn, aomksx, porttu
msmxf (66)
ldiqm (266)
llydxxz (37)
vdsaccd (11)
cbsdget (81) -> licrtwb, zovlqz
qgwhbwh (62)
epuqu (17)
loojs (43)
ovshy (95)
qhayeqe (86) -> opsrep, loojs, fvukbun
amrcopl (51)
tsncd (108) -> zygfdu, jsfqyd
oguxu (17)
skyaki (69)
ufxfx (25)
mpzyapm (19409) -> elygt, ltesfzf, dhqrk
lthoz (150) -> rwopuzo, uazwsu, ozaogat
xxtyban (14)
ggkael (54) -> gmjxxi, koevsvb
yuyhys (12)
qngug (76)
kazwz (92)
owysb (71)
eondv (25) -> uxggaix, ngfxax, ztdbvxb, jmytuxi, hkxfb, rvrzp, ppvsy
oyhqsok (65)
iflll (97)
xjbot (85)
tytsynv (81)
rsyxcdq (157)
vuoqao (102055) -> kahduw, lxmvg, vtwud, ktcffyf, ggdoqnl
ocvrlia (48)
cpuxdo (75) -> rroub, cvude
tpiwftj (482) -> cancxr, xhecnbf, ilcmx
eaoxb (2777) -> cfrbz, vmiykci, kllsasv
alfqryh (54)
gfnmx (214) -> ekfwu, ejqam, kccpv
daerl (14)
nvahhge (14)
rzvlc (19)
ktcffyf (1777) -> dhafpel, jtyljl, nmcewof, rhaoo, xsgyar, otetl, essijo
pntvfpd (49)
hkxfb (285)
ngfcc (87)
yqdaz (21)
qzwauo (49)
kdkobz (11)
tslbp (224) -> mvijo, qolgxnd
vlqqgb (63)
zsjlevq (175) -> bemxocu, builgr
xzsxx (79) -> zugkqyx, jubeqci
yvattv (44)
nhhytw (44) -> skyaki, nxqvwm
zmzobfp (75) -> ntxtwk, yhvdjl, xzsrv
sretj (240) -> wsnsqx, rekerpj, knciro, svcqds
awwhgzp (70)
adqnigs (72)
oipscid (85)
xsyqdlv (26)
eoign (134) -> aujeia, ngfcc, zobti
nfulfov (14) -> aivbhtz, exlwxxi, oqfpo
fqehxv (168) -> lgonp, vxufrto
impzr (70) -> lybwr, pyhcj
bnvlydl (63)
olzqxap (65)
frfotet (75)
ajidd (80)
qyvsaxn (30)
rlwoz (19) -> kjauagn, qkkhj
hysssy (12)
ptmsqz (81)
kahduw (31) -> qhotyqx, xhxek, bhakbq, ivgpv, lmnuii, frctm
ejdjxu (41) -> wazvn, algkwbg
ylfxp (99) -> heztht, mbtweib
isgky (80) -> kecckss, obakqyf
xclsj (59)
qhzem (47) -> fnkgp, ujipv, tuzkv
zaxbfog (47)
uekzf (1315) -> qjxikz, bptaz
gkjwl (50) -> pucdapo, zckdwxe, xqgxel, vcprhe
xqgqp (17)
ntrtfv (34)
ufust (68)
yvcanc (52)
jtqxxa (47)
rfumv (92)
qjxikz (38)
sybnvtp (59)
pugxio (62)
olfwppt (154) -> bwsgfa, lrplxk
ugelox (48)
oruhqn (95)
rlwmfp (158) -> bypqww, wuwhup
qnwwjwt (27)
hjmreq (78)
paykww (22)
aefjv (17)
hvpess (1924) -> vaxtfaa, wbnmb
dbziu (96)
xnfuz (84)
tpmqmg (22)
qrinzet (69)
ldrpjd (88)
pocwgw (13) -> glximrw, bhmirp, rcqkas, qdkhjb
sxexfai (9)
euhgw (208) -> xrbkzmk, xsyqdlv, vdtdmy
ulaio (203) -> pdddwgk, sakmm
vnmml (19)
ksncpee (28)
pucdapo (54)
ucnehpw (50)
btvsj (47)
veknoj (48)
papbxya (75)
sdzhsq (94)
orrfh (71)
gnxfwv (68)
grthhzv (244) -> dgmtgrv, tkojiz
dxcozh (35) -> phrpja, ahysv
vekndsc (94)
ujmfmiu (39) -> vrszijz, ugmhzm, sdrcc
jctafp (62)
bhmirp (53)
tmqlkof (28)
wyrfplr (109) -> qzwauo, pntvfpd
shcavm (18)
xmkegiw (28)
ydkhmp (290) -> cyanr, nofepy
ivkcc (70)
ujipv (183) -> gkrqba, nmsats
lnznpq (48)
xqxvktz (8)
wzezz (264) -> bfjxeyo, vkdytw, uwizlce
nvgohm (26)
ydqtt (158) -> oeabdth, bkgise, fjgjfpc
nmcewof (1182) -> plgjg, imtzl
bbnjml (31)
iweii (8) -> lvzzwy, nubqteb
kmpfxl (134829) -> csuywzh, ehrfv, bkfnip
dbkxe (34)
sfkpzr (76) -> lsszcka, manlcoz, oipscid
bbyoqzx (14)
uuavydd (43)
hjehgnc (489) -> ujqjrz, wulvcf
qmncyu (17) -> ofveqm, qgwhbwh, ftbiwxy
zzfom (210) -> jruttt, mvdkbch
cigew (185)
nozgflw (89)
trfjf (174) -> hskko, evbeo
idqhx (12)
noogeuk (6)
ccjze (60)
bedzc (43)
uymju (8) -> ectlgy, pchapba, tsncd
jvwvi (86)
xrqhewm (86)
ifijr (28)
tuzzzct (50)
zwrjdk (82)
ekvzyod (11)
vivco (626) -> okhisbv, biffdx, rbascuz
atujmm (250)
bdiftdg (69)
wqzxa (82)
jtoryw (76)
sttlowq (207) -> xmkegiw, tmqlkof
wqkoep (90)
sdloeq (14)
hzruk (47)
mgoic (36)
mqkqtjo (57)
gsxmqnw (68)
pexfst (44)
ycfbxe (254) -> tnljdhr, jfikdf
kenxmax (91)
yhvdjl (89)
gzpgvqq (78)
inglhm (94) -> qwqpht, keazynv
uytmyv (91)
wqgoxl (94)
yfxbu (32) -> jbujmr, mjlzzq, hcrys, mwfksx, fcaht, ycfbxe, tslbp
mnhrjdv (185) -> lmfclbd, sdloeq
gcasp (17)
jjgjvki (99205) -> suuppr, csmjozb, uexqjw, cckrzh, yuzzsk
zvqvvyp (39)
bgpab (1781) -> qmqpbm, rdwxvvp, vjwuuft, dlikiv, acaqfng
prbbfe (18)
gaalz (75)
robpw (77)
rcqkas (53)
axsimnf (403) -> yfyaho, qeyjc
mypula (58)
mnahxn (52) -> cxyxa, lqaveh
smqkli (81)
nkclzqq (44) -> bhyzi, okjds, gfsgzni
soyta (9)
cagvlf (267) -> ypcup, mbffei
dvuctqv (16)
hdvtd (75)
lexqf (96)
cuyweja (81)
vfteg (17) -> dclmckh, iihwb
fzuosl (94)
ipctg (80) -> zzyxzr, rqdtsp, esbdjah
yuzzsk (3542) -> ijlooi, yqgru, oullg, ekblpi, hudde
tpvhe (42) -> sretj, grthhzv, luqqu, uwqee, qssjswr, kbrwk
gpbdzes (96) -> dgvvo, zvnzrr
cmfwvem (23)
befwz (58)
mellhhn (166) -> vvzctek, hrlgs, evqbli
bmxolxn (20) -> bpwxvvw, sfnix, fxnap
rnqlzmv (88) -> tnlpmw, hrfbh
qeyjc (7)
jozav (82)
gjahajj (62)
qyfzonc (89)
ngjipr (24)
sepmxir (33) -> uuavydd, xocoiqa
qizpmf (98)
mroft (77)
lyeyx (61)
gtgovt (134) -> gqxyh, gbqbg
hrihd (50)
pygoqsv (55)
dxczurt (89) -> rupxxhm, lopnwz
mdfkbxa (18)
hcruo (72)
ytomr (9)
bhzfx (9)
mbgapsj (39)
omqhf (105) -> jwbdb, junva
wntitz (10)
zugkqyx (89)
ntxtwk (89)
phrpja (90)
ilcmx (129) -> xbtvux, agflbq
hhcoc (63)
bxggi (36)
obakqyf (51)
xrbkzmk (26)
sthtydb (22)
xvljr (21744) -> nfulfov, takbkro, gspffet, fqehxv
hofirm (33)
okhisbv (42)
uldgij (64)
sakmm (30)
zbuftv (62) -> glzmsn, oacnj
jxevsc (57) -> wvwjep, jilzdse, fxrkz, vkgfrb
ioycu (58)
ysuttai (72)
ttnoqm (133) -> vtopekt, naxtp
ereyjs (54)
hgksz (174) -> msuvilq, couhjsv
luqqu (112) -> yfaihrb, fizbyu
bixtvg (180)
kswafh (76)
fwide (24)
ghgou (12)
aujeia (87)
lgqad (75)
szvocp (11)
yivgs (36)
lnlkwq (216) -> nvahhge, bbyoqzx, daerl
qtcck (137) -> lgqad, ngtdwvu
wkeqlvj (51)
vbxzk (75)
uqkskjn (132) -> kbbcau, ufxfx
gacpvy (26)
ccbie (90) -> cmoty, uytmyv, dmiccse
suuppr (9751) -> uymju, rhpcgg, vivco
fqdolnu (16)
vcprhe (54)
iihwb (93)
swcsd (91) -> ltpmtif, jvwvi
nbwaei (61)
zdgyktc (84) -> jnqgs, uxfsb, xkzcttf
bimxf (51)
pdqzfg (70)
bomuft (785) -> xobszr, idpttp
kytha (39)
zyisjsj (58) -> woqoljk, pocct
hwycny (41)
ofveqm (62)
oqxnfd (59)
pnpsnjp (803) -> zpbrw, pbpva
ysekeoo (126) -> suawycj, gigtu
gneut (203)
zdrhuz (47)
qmqpbm (7) -> owysb, gdvbtjk, qytxu, wxfir
imrwgqw (170) -> yhncv, mklcsj
dymzl (72)
vzlzrt (55)
lfwpqb (93)
dirhtk (65) -> hrihd, udiai, bpsesr
donnc (33)
iactix (293) -> ulood, xkdjbxo
acaqfng (271) -> wrwim, ilohfvn
tuwedv (150) -> eiyiuq, ereyjs
mjlvx (41)
fwhhoz (72) -> rrrmaka, zkujvlv, fyaco
msuvilq (11)
mxvba (37)
smvskd (1262) -> cglfuq, rtcqml, zjnrzph
ggdoqnl (9436) -> hjehgnc, xnlkkx, srgob
aifpyc (61)
vwkkml (148790) -> hvpess, nuozixg, tshyvej, yfxbu, kiatxq
tipewrj (97)
pblqb (7) -> kouye, ibydam, jqdngi, tuzpls
oktgjb (70) -> lcbgeev, zwrjdk
dqoagdt (58)
xkzcttf (76)
zevrg (108) -> stzzli, kbybvzk
lomrivn (92)
grkzvkj (124) -> xemcuk, cmfwvem
uwvfga (63)
frxshon (95)
zzvhmse (157) -> ujgpnsy, idqhx, hysssy
ahsqaob (75) -> gtotarq, joszidy, frxshon, vfomix
jqbdh (20)
kvzmie (69)
oiaxzp (22)
spefs (96)
fxnap (89)
azhddw (909) -> smqimxg, mgoxhns, izgqzs
epssvr (57)
kxhvvgi (8) -> ihksnmq, wjsxcmb
etjwno (91)
tlwxovy (91)
capuc (91)
evbeo (38)
djvbdm (50) -> zzmczwl, whvpgmw, szqdapo, nbybi
mbffei (94)
uwqee (90) -> qyfzonc, nozgflw
bpzhj (251) -> hbaai, gfsnz, snywwu, ktlkx
dhcopz (207) -> hjbrfba, nlalji
jilzdse (70)
lgonp (40)
zvsgd (58) -> yzttfu, zavisuv
rdwxvvp (203) -> mlyar, lijszmh
wridnv (41)
ovtfd (81)
kttsf (35)
murnoa (238) -> gpbdzes, gtgovt, mqreb, grkzvkj, nyuxiu
otzinx (97)
bjjtifj (15)
irnjtjo (12) -> ubaxya, lomrivn, rlhmcf
zezeds (79) -> kbuurtb, pugxio, gjahajj
ofrogun (11)
bjzbqzq (54)
qolgxnd (35)
vdkhvyp (52) -> kfkfyx, mgiuz
rlhmcf (92)
okbtg (35) -> dymzl, eiohuhm
kkhlzm (96) -> wlavb, rfumv
dmiccse (91)
esqvkcm (59)
zzyxzr (61)
tegtsu (72)
kbrwk (124) -> tegtsu, adqnigs
mertvs (88)
awmmdn (49)
pknsw (74) -> lexqf, pxadg
fwtxvo (71) -> ibslyw, jnwdraz, ydqtt, flvrfdl
flwjj (85)
asbmk (76)
sdlta (11)
vdwfz (234) -> amtrbok, brpgc
exsugls (49)
yfaihrb (78)
oghyxz (213)
manlcoz (85)
mnoinr (84)
ibydam (58)
hjfucl (25)
lcbgeev (82)
ygglox (48)
xhxek (425) -> uwviodb, cenqs, mnahxn, ysekeoo, vdcmrrr, vdctvf
krtxpw (96)
zgxjjm (24)
vkhiz (86)
inhfutj (24)
qkxtwct (166) -> jfjvw, hbcpm
mfoismz (70)
voxemk (76)
inuci (86)
wllrov (200) -> nvgohm, mqsrwsz, gacpvy
fyaco (51)
ngtdwvu (75)
kfkfyx (94)
iiiupn (79)
gkpalaj (76) -> jjklma, ydejjeb, sttlowq, axqrke, ipctg
ubrrdtd (75)
fwskxq (31)
nzuhp (57)
npvuz (28)
fnkgp (65) -> vekndsc, sdzhsq, fzuosl
roorbg (95)
cfiqn (96)
fcnsfy (51)
idpttp (61)
vaxtfaa (83)
jubeqci (89)
uxggaix (195) -> shiaqps, xmjunhp
vvlimno (63)
txcon (87)
ocltuv (75)
kdffrsb (187) -> ldrpjd, oopnu
imtzl (99)
jvdoo (22)
yhzjjgc (93) -> xunvu, bebuqpx, wetluzb, hofirm
clktah (86)
givaxj (58)
fiprusz (88) -> bgydix, mpzyapm, xvljr, bnywvsx, snmey, batky, wpvale
wgvpotf (115) -> tmsmb, zzvkwsb, olfwppt, impzr
ohpkkhx (385) -> kttsf, ysnbr
eofyk (41) -> ctken, jyrzc, ysuttai
ubllty (91) -> qizpmf, husly
aqgumo (47)
zezbp (91)
mphzxio (33)
gfuyuz (209) -> jiizacd, awmmdn
rpxaf (59)
aewlgu (62) -> oazfz, aifpyc, oaoisa, nbwaei
coqek (166) -> uslhk, vczyhcg
kecckss (51)
jqlbenn (65)
jyrzc (72)
azgohsw (82)
qtqhwon (50)
furlcyu (85) -> lpwuzn, hnwfe
evqbli (9)
zwvhgce (121) -> chxgqe, hzruk
xsfryrh (21)
jjtafg (37)
acfdkr (17)
rupxxhm (91)
nnelc (342)
hdbkw (43)
usgpgi (182) -> ketopn, mvtkwn
thxqmj (81)
bgydix (16136) -> tpvhe, excdqtl, yjvfni, iaayhc
pxadg (96)
uiryg (2879) -> aibtig, sepmxir, ixkpaf
exlwxxi (78)
vecnb (897) -> atujmm, qrynkpt, trfjf
zkwnhn (329) -> oorvvpt, zzdae
ezmot (96) -> bykuuwe, fiwvclv
vrxkr (37) -> jxevsc, gtkii, nlrlj, kwlyw, fqkzcq
zmstcy (8)
axygpr (13)
yzose (57)
kproiw (93)
lptaikg (82)
cmmnjch (6) -> ewwab, awwhgzp, tqsrg, ivkcc
qpgphk (33) -> lyeyx, cqfsg
hittl (20)
wbnmb (83)
tsevkec (54) -> yvvxtg, wqkoep
mwfksx (216) -> mbgapsj, zvqvvyp
bvmhqar (224) -> epuqu, gcasp
oeabdth (17)
pchapba (70) -> kqaua, ljitswv
gsckda (89)
gtbjtpi (265) -> ovshy, xpttnwd
xocoiqa (43)
woctu (56) -> qrorhfv, axsimnf, wgbviwb
foxvut (77)
zerhdhs (150) -> xtidu, yuyhys, ghgou, sqbxzl
rqdtsp (61)
dizqtw (103) -> ieowdj, vgkhk
ebdva (718) -> vgfveov, zerhdhs, kxhvvgi, oqokji, lpmnwh
ikfzj (212) -> nrfyua, ekvzyod
hcrys (63) -> foxvut, oislgqy, mroft
vkgfrb (70)
bwemy (92) -> oaqkk, kvzmie
yname (1373) -> qhayeqe, dxcozh, dirhtk, zwvhgce
desuqj (91)
bnywvsx (19757) -> pnpsnjp, paunv, hxeqn
wiasj (34)
lhyzwtf (35)
gztng (22)
szqdapo (54)
flwbwcq (142) -> xekft, jctafp
ijoaqyv (91) -> ldcmzd, sambc, aewlgu, wrkoi, xtgmmc, cglyptu, qhixu
knyvyft (81)
ngfxax (139) -> uiilkiq, iijfq
atqfhm (92)
masvpfj (184) -> ifijr, zzonk
yhncv (54)
wwhyd (95)
oggljxs (314) -> awrbrc, yrysmsi
sdrcc (56)
sgqhelx (60) -> hhcoc, vvlimno
snmey (84) -> bgpab, xflsc, kidvt, rlurjca, uiryg, eaoxb, dulrvcq
qpchzkg (57)
mhaucon (2652) -> smvskd, wkgyfpp, fkgkcwd, jsaujq
brpgc (12)
vimnt (91) -> rwhgw, asbmk, lvarp, monhu
excdqtl (378) -> hcsjun, trskdr, tfotbwz
uxlisdh (89)
isbdm (1276) -> aqgumo, svjnd
alsfpfg (21)
zzpwgcd (68)
glaosn (86) -> ptmsqz, ivvyjos
fvukbun (43)
rokri (55)
qrorhfv (93) -> redkli, thxqmj, esavxwq, knyvyft
eziosif (33)
jqgfu (40)
nbqaqp (298) -> owxski, nyckm
hyxtojc (5)
awrbrc (14)
ogbov (15)
rbascuz (42)
kdzhiq (63) -> kenxmax, tlwxovy, zezbp
geapi (75)
oiozpzq (127) -> uldgij, kiawm
fzafkj (88)
zejcp (76)
wrkoi (124) -> capuc, wifrwut
dhqrk (173) -> zdgyktc, etcsuuv, uhwlk
jtyljl (348) -> bveilrx, nbqaqp, fuujiy
otetl (1340) -> patlvg, gjhfseh
mnufo (7)
cfrbz (117) -> krtglj, jcoyk
lsszcka (85)
rgdvqu (166) -> dbkxe, clwtgt
yjvfni (1179) -> ofnqgn, rsyxcdq, cpuxdo
gfsnz (14) -> ydtykm, tjwynpa
knciro (7)
sfnix (89)
cqfsg (61)
izqxal (142) -> kxdbyp, sqljeh
ivgpv (1040) -> ubllty, qtcck, bmxolxn
bazwto (49)
twimkx (24)
evrtfzj (19)
ofnqgn (19) -> qrinzet, fkitgnx
nrloleu (93)
ylazd (201) -> jqlbenn, oeixw
hrfbh (49)
dkexo (146) -> nffvt, llydxxz, bgtzw
hibjkps (106) -> cmfwwv, jqgfu
oacnj (93)
inelfwo (91)
vgkhk (76)
cckrzh (6841) -> hdinwud, dqzkic, vrxkr
"""
DAY5INPUT = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"
#~ DAY5INPUT = "0	2	5	0"
DAY4INPUT = """pphsv ojtou brvhsj cer ntfhlra udeh ccgtyzc zoyzmh jum lugbnk
vxjnf fzqitnj uyfck blnl impo kxoow nngd worcm bdesehw
caibh nfuk kfnu llfdbz uxjty yxjut jcea
qiho qif eupwww avyglnj nxzotsu hio lws
xjty usocjsh pivk qnknunc yjcgh bwya djw zpyr
ycfmfe mgq sjiomg nfzjul bjwkmgu yvsnvgj dcjupu wzz blmn
rdowgbt vpwfdoi blzl laghnk gsa vhnpo cztxzlb rtz hvwonhb eciju pfjtbo
bqs bqs dbutvgf mmzb izpyud rap izpyud xlzeb mnj hjncs
xpu vwp nujcos piu irindir tpmfd umtvlm gznu
sfpuxar qcnbte omouazv cnh uaxspfr sepolf rusafpx
xbmaf iceyqqq sabpt gliexel muubepe qqiyqce fmrcc eazk obkeonl fmccr kgk
apg gbycwe gap pag
gagv saqbk lwtllc wnhzz khxsjc
lgc alen rlmsp anel gcbvg
bujlaz rks rlqf deknmee yrp
scqvl weusbc bgvaz vgg cjwsfno vqy zbq aqy tvf bgzav
hbki vei fxdwljs myjuba elbsib pvy xxjxgi dtgv
linzaeu qbwdke fdg pykw
qvtdd aco aav bpu mvkcuc kjfj japgfki jfdl gem hog bdzsiea
wpbigkb lzhwba jssjkn qvb kmwu qddv
iny osyvqnt tumunzb torq bdeneg wywank poza ipp iggorw
tuko mhdbsf vmjdop jomaqpj rcdsud hmgspr lsas nzmwc
cirkjq nmjuu xtgejv gtexvj vjcmtqq unjmu
xsdmezq xvqjvqp exhygy qahju hvd qadmdh lok
wvvys kax rohrrar rwhnvi lhnmefp lsktouy bxilosp
wayf diobnl zvu obnidl oibnld
cewil ygsf ffzp ruxhu vah lnvwt aef lnnjc kgkb gxtlx feko
uti epphrin pywths cpzzh csjei nczhamy gayxmb bdcytq xkx fgmt
qvzyuwi dwo swkw bwjdrn dasgd ijgw vzabaop yefyhmc wgij
dyg sugrf vid etz weyqg nyntx dwfgwm khon hnzzzn xfyra
ofbh bdrsk rdrjj elaxvk jrjdr
msxau rsocvx zxdda mxz lknl
qktaywx dirpdbf unqnd wbrwkuu fvmqwl emxr big
xwz kvsydc ayokjyy qiah omw neo htltxx fxhwqwj colqvbb sxmo ephfkex
ncjxoaf fwjkc czmhv ylg axcjofn dvj bzqjku opvcr jiwzucg vmhzc
gmmnrt zqar twdwrg qiwwki fcbr lixm hjdwwe moiva
roinlxg cxeezve whannk cxeezve pyoj boweioy cpkgxsz
qkct qso xlb xyy aellfet rzt cbboow devfb nih fhbfxzi
qyc ltxia alixt atilx xtgrv
svruz ufvo rvesnxv dik vzurs jjg idk
xeudhrg hudn cilo ljplosb
kpb oyzvywx vldko qhfkwod bkeutk zqcqug pbriu wqocos
qkngzfy whobyri aze jvipdty ocirbep icqwc
kzxxlab sjr zhymws xkbx
nnxs gkwtld dwhkry snuibq dtdl aicug bhtlfzp qzk jctos
regvro mxcq hqof yraucxi jhkol iuxineo pbtnk rfjwc szgjpr ndqqj vfgm
yqrfox xoqrfy utbryu utubyr
jdubjt wqrl wnk rlqw nwiq pnbn qinw uaff ftdo htfrav
rum mur umr tij ovbahl losao imawwpb wadhww tbteyqc
napxd kzeiqcp ppgqucm xkityt frq hugrp gjgtt gmuqppc zwqme
xyuzs ysch howlzgu dkqppbs nvbiz mks mtxv vivouex uvawq
ffe lfsn nlq mpulheq ikcfo wdtz cnwsbph zkib muu
bqkxav wtecb lxwdhr kqbavx aqxvbk
czwswqx ldkxapd pfwd bdkkj iqohla cwosw ihqpd pcc ckhabbn
foiip hau rbqiyhh htm omeubgh symh evfcqg
lqx xlq rsgf izu esetis
npsrkdj fvulgkw eovw mzr uobcze azb tij ihoer ehori jit wknsqhm
gnrksh xwggt oosi bpnmhx qqaa mpmryu jhzyz
yad gbexqcr gbexqcr gbexqcr
ldca xxhznn twyy ytwy zhxnnx xfmpi
floioot kfyh dhibv ezyznar sfg sfg ezyznar
cinioim iiocmin ypla aypl
mhwcjbz dftuqsy wswop eizbf ptsd
ehx mlh nfxgfkz uuw xftmn ptlkbo vsnyo ttwce
oexvf orcg cncnkfk comvhl
lqewsj lyulrcl efixd qvd fhznqnz yvrkwyi xmhgc vzbp
dmr wrxqh thcm giomp rtvl ssc gwq rbklw hcmt fjvud
teozhb dmzwfv qkq pvcqfqq
hvlebc qqmg repxk zwrjdx ztruwb such tyligs ybg
psa rqznokd lgc jstqres yiqt mbiody xazb xjuk dtb
lea ncm rnh myzqzwm
wjml eums ueflvbr cjpgnl qduunu zfxaai jwlm lprzzg vrn ttetyr sume
uwkgeu uiahd plyewgi vveo nwhsitz mcitc uvk zsxehgs sewl
lnbdrka sgtivn sozzq mgd vhxfnlr twrfpk
gadphmk mbx lmlbrf tsnehnr lawdpm fnima gxgl
umty vrn dpow fsnnpjv fsnvnjp nnsvpjf cioaio
euu uue zeskmtk hob stekkzm
ypqpri qwdju ypriqp iprqyp jnoxqa
lkppi ingfxw wlulvp yhwrli nxwigf oyuhq ggfslx
kdd ypvr pyvr waw vyrp khqq mamxca bapq gobfm
iuq upvdpv zxef bfwns lmq lxswr kpsqo pwde iaaou nsw udy
lgzo nil ovgrmt omgtrv jrqp pqrj lit
uumyu iiakfj gvdtzz qbux yxn ejs dvlts
hcm ghutxq zswi tmyhqef hgxtuq
shkhkdk kad seubeax kdl mzu
cpykgr skx rfhpor xsk moyhlai ogv ophfrr dxipuuh
beyw jvrre opodn zdoajhx fhg ijs drczy drczy hjungq
jrzieja gfg yzdn yxm wshibsn fgg
xtylh vxscmvp rfymq uzhpyea spxcmvv dlni msj yxhlt
eov awql miv miv eov
mmvrfbg fjiyf hvqz zpuqmbf fszyuz ldfgni wemfjl fjjpl rbnpy rfb
ppzpeh nam ntv xnchtyk hja hpepzp foj bibvx nmmdlff bsrkp
qiy qiy umhlnh qiy
tyds oepk wae tdsy sdty
ukawr rkwau ghtjhm axy
wtbjiv btjivw ewaf hwk ttq
kdpun myve sqv rhvpy fnjwt puw ujhf thsp nkdadqr
vyw wkkpdpy xlgz lmmcuve ncuq lmotk
pmsfw vxd jpe qxlyasx ejp gwuv
pmgyndm ezofbvx nicbwrw kwnlj yjvnas fdpkfo mqcsyhn pyjpf fbexvzo vkftm erl
trmwvk rywuzoz hbidea kicohfz heidab deaibh
sogf govd dknpk vxrvk rlm vwhjk
xnxbfmw wguzrhd zbmkz piwppa mkbzz xvwrdgy flusfqb
cgduq hbnwr xfx mrejb ckw zkbaihf cloow cwk wuvthv iwqctx
vugx qbucd gxuv ocb cob
ilmet fbelxxz qratdfn unoj hbc duv srmikz
vnzuw zgpbqgf uzm thysyxd dinfh bgvr olungg ksd dsetwqz hpg
omagsf zpr coa kknx bzithq pewp flvoz xiiq weojqr wpep
aagj gcglqt gqcglt xbfx dhdx lbx
pljq plxuscw ilh wfk lhi hli fouieyw
hvnh zvm aqy dzitirm veq ctux
lglhs aqibdii hjbn cfgc qrg pnbntcx owoks ebz
jozngde lwne mbo omb fnyzvvj gndozje
bbdgc igtdj uhahgp sqduko
uuspedu fgnspm ewc slly jbs chl heanm abqijx kadvgxu
akfsft skna kusjqr rkqujs
erc vrljpu lruvjp lpvjur
iors hcdr fsqtcj vop vmn dtqnz tov oscjlw cdrh ctfjsq lrnts
fxp mczo sjlcxa mzoc jmsq hcxybow dmrr bcoxhyw
aac ewraerq odmxpz aac aac
zzio zebmxa szeej poordr gmi owwnnh xfx rzrab lfey jesze
akc yyoj vqod drtne
joxhvyf ymasnbr omouvq isxdrr
qyi ayrkzu jsk vqvvno jkkuxi zufnnwu mrsszdf
ocqi htfb tzjna cdt wkzhynm eergf
yokzugl usyuqu qvotq uweqyow lygkzuo kpmqmb uglyzok
glvshl imqv jrv xlpnsy gcg psj irtiamg wkl
bjcpc nvyloa dkkan efj okubpc cxlowm eone kmpny
cyxqys nmuaftv gqxj gtvsc
beouh dioxiah kizdy hyi cozrray rave fqxmxmj gdm
frjz amrsat lxvhzj azhevtu vxlzhj
zwmnrk sbk txzrcsj sbk oosgfej cvh zuthibi onvwd sbk nhwpzq
gzamt vraw kuk ugayl lyaug bww rwav ijah
bdjirxg vifjr rhbxpa oao yrhjxoi pbn
navb umesiys yhix phuhu aekkciu nlnsiq wjf idqdwp
cmhw rsu urs ziprlfe
kyhxitv cgty bnwjyq cygt sgjn pdab imarvhg yjbnqw
axaa ejancv yau njpc jvwy bpft kwjvg qzrbvtm diu njpc bpft
ambj upe rmqr yudbiqf krudp pqyf
tnb mobnpv vep ohxoc cyip wxyccfo jrbi rwsws kls zlv oohxc
fjh dmb hlbq bqc jhf kax suz fjjg rkpc
wjnn byfirm goeyh xtjmdka
tgyfxx hefpxln mveobqr yeo ftfn srt vim vlcu hevoi xtaaff
imyql xotcl poql rlueapq bkwykm hlalk bkwykm
gkec zff hbmtq rjxjbcf arerlu pvz cdaqi nijmhv uodwjh
mpctof mopftc ksfbat sbkatf
nvdd jub bvi kyggdbx nwtiok gjt mgsm dbhsn rzibgjm dvdn eqi
ysd iirp dfgzza wiyeoou ysd ispkv bcqg wwzqgq xphse
ntq ivposb gsd ezl tlkztp lez qyurp vxsmg dgs
wijs rydbj onm usiyqzb hwrol giusanb kewukl yziuqbs doojam nom
lfacyy xwwast truqtt tzneimn uxsydc ktu eqyaj ndszak
ffleooc kikif fohgop aucy moubqxu
iaxc pnwexdl ncy vmwm xrqoi wpgftq rofx utyzjuf stdxq twpgfq
ppmlp etsvi cjdx poly ynx vfxpslg mqjo qnpsage flpsxvg jwsxiqt
lbyhnb kflrpeq ssoti webxr embbjd kbnx ubzqco
khhc vwuqzb ebocbko rwmonkz edfqn hzh qhncoq gbwdi wjeg ocwow
ghzhd kcxblp lzwkkr gzhdh umk pblcxk
wyajtw jiff ouylv sni lwhlrg avqjiis igzx wbl lhrwgl
glhh kaxha tqii hwzx rgic kaxha rgyidmt qdgxfl ynjc oibfij
bapj bix rjniw ynbql idlvnmt wynpzbl zlpuoix kvn kakwys
aldpxxu iojxp rif xbyqtr jffdvy qnrq tqwsdiu
ulssco ktbymjw bfj zhkg zgc ctyri
ilrmq wfahcgk mrlqi bguad inj
cjzc rekuy ifr wfkg sple
cvjkp qbmumnp mprg ltmwxxh zpemtyb ozzssfd ksu mgrp
nvc sxp mpkxz bhlctq hguaa yrdkm iwsgfg qjssh gobbies hucdh
jdxrjw qmo qmo vobhnu
dnjib wtjp rfdjqdj skpvrb vkwevb kxxovp
fzi kicta zkuvr rfaawv ehklq cfdjsyb tukahwr zkuvr kicta ouq
aba ytdguk gqmpn hvxabff hvxabff dckj
fna wxyqhxd hvy khsu yypoyy lvvue medheua gim slf drdbeh ikihf
jquz wwo wwo ghlz jrbvb jrbvb
jwzvkl yjw ouwla yjw ouwla
zsvlgyf rzqbtj qygynem ukdgjm lbsyh tmdzp fbcaim eymzr
pvw sbs dvsa plmepl pwv ayxk vpw dwt
inayadn pnti yzhxk azga gxq aznbciu gjnmyqm
isgf ndqmk beyqq ebyqq srtzxo aiiw oqfuwp uoqwfp buejctv pxbk
pzl irv tzvzdb wcy eszm ybwiw ycw riizifd iybww
btpu cua azzqffy owcr
ofwq sqlpzat lozdxlc aevjmpc lcolzxd wbbysn qwfo vcrx gdzgi
dbpfmxu ydsxwl ijn svxtop csep ldqeog ffye zcrl soh aclw
wyiyyhv vyhiywy obgi hiyywvy
ddvaoc lhv spurn rgxyy onjw illvn yryxg xyyrg
vid wdttqq kajr myip
wolqlue phlunpt dcmmkfm sgxk dmmckmf sfng jlbsntq dxp
zmneyho fswj xdgsjc oefwjdi htgxvbd tgqrq xodoa
ynw bygqdnh hhmnkuw cojqrke qszzdjo orskwq mdfae asabn
vvpm vkj pcxghao caoxphg axhblxb vvmp
txox nzy eqn zgir dytsi girz ffa ugjjbzj brob fll
kbz pukqbd fiwmuh umwihf bkz dvz
vgs vejs vejs vejs mbkyjjy
viqmnmu bitkyw nddnk dknnd cldnpp hipub plcdpn fdzzpb mmyomn
ndylnfx gozlrx ngptk rnpteb wtacx xmtcjy xldha
fey doyxis ampmtr ycqh syw cqhlj hnngx
dijf nac tvkq ayo akbj lzmngdm wfxpn bpyvrf cvdqpa
zsofz lhho hgat wqskga mnt
mylwm zxsd omzpa waz hcrr lxmpq jsw sqtwak pzoma
rwhgsgt ysdq ztihici mpwcawv alkqg wsxiwx
snldn bcb anjdv cbb awsscc cqxult hjmjew mcycb fdpdg sesrh
kukrqm fawafz qdim wyobtqx bnvjnqg dcvqxta yptr nnpu ughldqp duo zafwaf
knb yjqb bscpnt nzg sqeu zkahna ttuf nsbtpc ixwit vucwj idix
bfqyx xlnpc ijrxu zkqi kjxtahr fgag orusms adi bfqyx bfqyx
dqddc ncbv bvfk hefikb dqddc hqjl otpx zfiu
ntkv qunrzx eztzure ctt rjo bkdt znvd jwdf gqhf mmhrzgt
zeavm hkbf rawqwuf pis dojlkt vnjhmi uvk cufmn qginezd xyut
hnidzk chlctc yst pepd dxntbxg vqk daxfpmu wshyddl
jgd vesqgo bdyqy igl ahstdm wjtd lrtkjsv tjsj sccxbih esn gkkzj
iisiswh jll rhlaf jqwwgfa wmhyo izva vrg zjkak nlxxfer rvhx
mkrkd jlqtpy ukstro ktuors wsj ynqpbp kpiyxzv nxeiwg xpzvkiy
jbr gnct fwklekg cmfqnm ctn gqobrs kwht
pztmjs yiffc kfhsblx yiffc yiffc
biezil iiezbl bzeiil smocoju
viiigm gmmmk yeiv dxzogro qsmzsur hukzwjn lcle syo mdj uruf rxfseu
extchsd adeff ouikoj fyaclr rwwvqsd dooe tcxheds zrdqqhm fdoxv kbxi tlcj
aycnydq qlxhka zoi shplo qll
bfry lbwckm ltq rbfy gpn vojp ruj dpxcve geq
svtvfwh lca lac qia vhwsftv nookdfz xgjiaf yvcdlt
aspgqym fryuzhx bbydf tbn bwutsc fqgi zij lmxhog qnmse
rbb gsys volnas onvlas lonasv vwjdso lnteapy
got iauk kficn jvfuy yvoe jcxwui hyamqx mke mwh jcxwui hyamqx
avutfi ggmha dkopc kothnnb syoi xsd wjedywy
oziejyz yzeijoz hnthyn knj juuq qujtp kgq bymlnlf yicf
zsejuy dybeap hvowmvn okxb yoi epadby cnzjk xfwprzc
lacg iiix fblhxvf nrkkol lnafzw qspzsn gvdy ipj zub uouseo
evukwkh ycjxxc lptwmf pmd izxdsos zrkavf pgjoy zwokg mpjiej
vqw ijwoy eaw wvq svmcq ccxi nyub ynlq eqornax uprt pygfe
plue okbbm btvm gba kutn jacjx ysqt lvx pcxxu qcf
pyw ffjfudq bvk hsdwdva fjnivhf odbmw krpgrj
hziesm bxa dceiwt tmvivjk snl fkh dahsxyx kqlhak lurtk
xss sswyxrg yqff dbkx kbxd mpzbmnl bzplnmm
uvz pjm ilrol pmj uzct ztcu brhkv
heiz jcn syjt zfvlvaq aflvqvz amcjh rxnitw
cxl nxvrn vjnz aewtr cxtko nnvcp ltptd adpxt zvjn fntklj
aymmm tuirj hzngq zhbh paqs kvpfo aqsp kmo acprw sabrso kdqmp
ndqjspv mmhp pndjsvq rti usm
ije oad mvelyg jadz ekm dao zdcmv
qwww tmwmdbb oxxfoza rgmf eonku brh gcgiuoi ojscn
fjedeek ohlax fiydku rbnxpg wfivg cdgs
axwbni hojye mwfe oyqknxp whdgfy ihku mbhr gagnz hehagxj
hibautd blnayq lnayqb gepml mgpel qunw
ircx oeb kujtip zbu ebo cmmn
upyqvot wbponp hnn vav avv tvrky omm
yzqsnf agbfsw dbxoya sfnqzy hqrxek qsnyzf oagyerm xxhukm
xzvk mvcwz oujr hell hoe xexa dqlpqt xdqz ucola hsvv tcmybhl
skldxr mzyol ybzyzd jnnxb rxncdy nkpwy fwlnsw omylz oiwieu fshv ngvha
jkwqf yxrox hejfoq orxyx
rijken xiwf mawqcfu erinjk jsi yyg mmu mdkfqb
ornjes krp eornjs enjros pyqp nnwwjl
wzd uqqo kyeli tikdle aykdjog uiz rbpnw mjxezf ihiz rlgyg
cjm ajqgvkz kfgyy dmczlc mjc kxcm zctyqgh ymsk jwhqfd czpqgan
vxkzvco owo qogj uyictoj kfr pyoo ejrru npluynx bvv jhhzu kuciwc
eqk pcsly kelu arzgoe trfo fotr cuaax
lagonw qvcssqz sdoklh uvovi sfrkmd hnvafj ltg wfjj
viwbkm hpwe kzzwrbr axjtlq mznin wwpjg unlwur
nuzorgo qfoz ydisca qxdfutv hzg
nqgge tobtt hjocx ntyqyi rxzkynw wrnxzyk ciscy trjt ottbt
yuii srawx gljxe eteogz kcu jlgxe tjik ktsnp agudqok jwol vfnyv
vgicg dhnrmxz sjhozy hlalx rutwq
nyoyoje kco hoyam hoyam tta iflud amh gdxcsj vqr fvsqcgv
xdmbtph ueen cskerl rxjvpdc
nricn addljzg obq rikez igq bxygkmv qmgojou uheubk qor
snzd ztusvr vrstzu mceddga hgu
vvrbfjg mcdhmsf ldtwl otuna gmjurrx jgrurxm rxmurjg yrioq
iotkvo sftfvn vvoit lllju xvlg rdsb ywmdf mzxigu kzq
sgqw gqsw lqfu wgqs xpiwou jurgucd azq wgaqpm
ijntzi chlnfj yjqatz hjflcn vys ofq oqf oadthe jrfw
mmc motjo vcwmod rpaszfk zgkkua bpja vjb htrk
bpfvvka kmger mnvvfl hakudy yfprdoo mvnlfv rgmek evnwg
mykpu juavkn cecdvi aszbi lxm hmps oaqoif
fshizd fsdzhi lvcq hhpb eavwno auqlwz rpv owcdojx amsmf qgnddd
pohmcn hlcxk qsesxh rncr
fgyrsis ldem avxmnh frpodq oefzn
plfpu qdyojz xdrzrjy kpv abkh fge bbnotvp liikmcu czvwl oyh
ovha muitw pzy edfjoo fhsxuh dliyruc dikcd cqem ywfy
exyry jtzqn tscr qbtxno cikk poqgr tnjzq eofe sxea anlikep kick
zcie purpw dmhhms bcdo prwup uprpw wfejgjd
kwtjc cmixp dodfwj hcgmmat pkeyspo ubnl ajxvj ffkh xvw
nvlgq oduus psufiqg lrwpn dleftn xtllqvf usgz
liarf sczsf sczsf wky qtzq qvve qvve
cit vtjsh jrhkyvi txj urmq hppx
rhblmxn rhblmxn lkgow dylurwc beyk gfcewxj ehpl disoe tjbjy lkgow
nbkrm jvk ffux ars agns bebic jzjfm kmnbr gptvtsa ufxf
hrlvup jaz tafyr qcgq wkd fiz bgsrx jmtcvo qkbvj
eontk djf tiafrng mtwat puainel nyjoh meynxbf eqdw
aspvmbx tgzuszm fpj xkl nzpr fjp vnomk byx sbtov tnu utn
ldyww gwmiddv hwyh gcgsdit gtgdisc suufl xsw dlwyw
sye dgbd wyf ixqzthx dgdb esy
nsdgera fqz xwbdgui ngdgbcd bcn qrdxml cwcmxws tncm mqsodj cqgk
estayas cocmbpv cdcf vygtswo aplwa estayas
ndc ndc wntr sfls sfls
gse svv esmi lcdii lnr kemrk gnk ildic blnqy wvn
mwlpm awkr sxsudub yauwww hnktbog fpnqc nmxoq yoparu tqjpkug nbipft
czwnkk hrodtmx yyzpil ooqjb cvxzfh
kwa wak gipak gsgrw
jyy fja jjk kuvoqdy urqx
doyu chgn gvtxi qjdigvy kxr dizwrjc sll zenl yyblj
epxeqih kfi hlog pakk kkiidrh hiufw wuhif baqzxzi bgcd phi jzjdxjp
hllhyad sodc nyrtfe kygof hyyqi txddqg wcwxvnt ewqmj wwv
vxymuoe caat diqwbo vfruxdf sqniefn hetcbl nvtttu ouesb
yvoez pvthzc tdowuci wjijicn fhpmq kfobag yctdwj
xaugkb rprkg tidpx pjk tpwwm pbcfhr wmwpt sfynrl iouaw zbnyu
auakc culuxg bffg rodyhea ixlmtfb jdurl szoa
xgona fjzho buh khbvti ddh mgj ptgaqps
dqldupd udpldqd poku gfgpcg zsvk grvk kntx jih uwvxdvq sivk
mwdnq wmqdn uzto mdqnw
alvfm qxqo thwru xqqo jilnsgs rnonk fwntuby ogbha
gvxlxyf cdpv khvpka kgt gshlaa tenb
mtgvvxh mrjrsd truk rrerzx tujweaz
ozepw gsqkr rtmmc cmrtm
spnthg xhlzuu xwcrxz aqqejhh bpzh
ectdftk rgp mkp vxp pevriz wkgfkaw vfygj peg gep wjn
bksbu ywsszf tsbrps vxicr hfustju ynnlbo
sio urbvf ujezjk vkyc ukjezj bvrfu qwwgqmw uqfekvx bzipxus qfumwh
druru kycweog ycmef rjyy fkgp
rmf ifbip rsztco coju wlr bfbmsug lwr bsufbgm nwmp
jjuxtyd yif rkldsvu binq spepa mfg aszm
ghilaau ncm sgbavz omzeotz azukf bgjw zqzo gjbw pld
gtog iqheik budeu guvljmi
qqlj jqql ttk xcxu
cfq cfq kpagib dxfxufw hhksbjh gpcp
xkeax acnia jjubfc mhot uxlhh gnkj pavta rciondm rkquh xudqian
wqhqzg psqh rnnc uujlgq
hpjpaoa maa rdndl xewqj nmagwx xewqj hxuyvou xziv rdndl fbxmbz hmfwghy
dtwnrca hbfcptw qrmvat sdatx les zwizogq
bodiwzg sgoas fsf wgkrn zgbdowi wfkz
ngcsg grtao wcfxpyl gngcs fxwycpl fkpt
txvngo vxngot tkoap zqjc qzcj oeruix myh ihgdfik qtt
rxeh fcbnoo rxeh lve wvoc pmnxej dlcbrh rztt noibg
zyvq lwxqu oyjv bvidmf wxuql
wzc zcw czw dnhkvrg nzslrf
cfgl uwhxu qnsfmt tgyabes mqnq nkitq hmcvxlt qqmn yzmb uomqp
lwziur hgmdmv zuvipkp vir apr gfaq zeo dunat mqgafzg
prq pqkr xlrw njf ncqni kgpoma cmtklv
jwfuc poz opz fuple
fgleub lcgnifu lkwo kftbc onvwvdx lukpod xgmh rnj
rwqvv ezjmoni llq ekd cdvv kzcci gzsj vuipv fnw
rtnua gbnzg kqtogns iozzwc kjpzz kiiurey yzlvzx cpy xrue
fexcjmw ebwssx ewbcgwd uwolou nfdhic vupiykn jss djoo xftbkgo
idf ipvmez qyevwd wfsjxja dif dig
szpbtsa bssaztp sptzasb qppgz odur cpmn wpmg
pxn zjmq rbnr azwstzm mln upaqyty nxp oge nlm
bfaryqv hag phtvh ypi
epeeog lip zqio wuehlnb bau sbd dsb
xbrrp sej agrqnpa aarpnqg bnwyi jbn
uqmsvd asmuyy czxviw pznnmvc
sddwmek wnaea iwphupk sabo
cingdks ksh mtyip zltgafm dflkcd wbdnqup uokm gmxpyd libz svv akce
qge ewv dkabkmb xcpi nrkmsu mkmb djvamg mhhrwjh
krjt etfhm bxzatw zdkvz ehov seyxbw mkiirs plzoplu sogmwb wodfcle
qwea adibdp emo homrd pjcrhlc eqaw kqsrp rphjlcc
gajzo nwjg qxjra jztcnir ijvjwez avxb afz zyywqz kcszgh elmlkfh
lbz ozia bctf bumoji anhil rta xvit
ejybire ypjl qevak fzalx mlh qxlei zib
xmzas kwojjz ntrnrw nbmxlv mdgxs xjhxg suo zdcrxl qkujisz pxmu
eezyd unrtm wyu vhufvto rpb isfcy ygh hgy
nszvbzv ebtt memrsva ebtt qwcaq bhbas pvzfbov ppjbdy nszvbzv jabvrp
rlo zbmi lugvu yeby
tfcd tvl faaq mnural nyarh xnxk ctdf bodz
vwdrhc gub bgu fpcovx rcvwhd jukwsue
aekrhi lpknnrh bett tkib ioqrap igwnst aekrhi lhha
acg mknhazp pcgjuk tajplv
masq fyjkn agq qhxbbl qga npzj fme xtihic rntisg iqv aqg
ipagh fjth mswztpi iexd cocojy vhqrla joe wrsrmw
njztu tsh auqrxca zpp
jctn webxi haq irrr qox irrr webxi
reaw axmnvd voakf lnz ftbxfh zjyxzl pryfjpv sistgb pov mshs
gsy ctsngl ptmnyx vpjx zpvtori pfu ioycdrq
aobdtlj osdnrth sgqe geqs qegs
oamrlxk ygbb rkamoxl nztl sarbmtj yqupjt plu sbtarmj vpa rxea
yvhgp yznko epwpza gqrsod rilukp cglhomj wnaplu ugvdko qdr
cggztg ajw gggzct ubmiefj kpa
rel lvasbh kobm mdnzla pwnyj ehep gzx nhjdnsg rxa
qaz gook rplqwh vsht
dhe aneq ivrn awekad ckcbt zsqca ehd rvni oulwfuu
oxgzzow wntz tkqaoi oxgzzow lwkdpgy lhd aekjasp tkqaoi dnhaw
alxghco cpanoa onjh hyeyebe whxn zfu zozbll gojn
zdqulsa dlqsazu zqudals sfedw
rydtrsv rrtvysd fvyza drdgh lsfzt blnxr cnxe tslzf iijyds ylcxn
cczea nxx kwol kopaza wuvr cyvoo whlicv
zbmrwdq tlzbevx jwzpsc uvkwpd bmss rbzblj
jogx jgi gji hypmtkg ijg oscjv
flkoqja kwmrqv wzehel fvmcfap mkwqvr ivwxg jqfwdvo hweezl
vgjg nzucho nuohcz ggvj tmxci
fqaqx zeybhtg bxeic lftuqp wzuerz sww qfltxk
keiy myrvp blkxcg lncqmsu diittlg fqrf digrel cpwrk ipan dkxb bymlzo
owm irygdz pyhj mow wmo
noul pbvvt zcv ueqyjl zhetlw lpjfhli
felvwb wdykz kyibdz haq qkouj vuav oztyqh
dyxo njcr hcuk ysrr pucw qbajztc
ooyaz pmt hqwu gjx tmp tpm pwz
lyhzajz dfot avyifo kdwka pwypcep kyyw tirlku zdpjmft
aexle hfxo dacwvcy xsiotyg cifq ibupshj aktt rzvf pgafj
pxubhw ibpm jxtxg iwnssf osbpj
exmtfyx blbfg emrunru zkuhoi lfzn zrj unmcece phuppi
icomb rmy mvsqqkh zwjubz lumq wekx
cmdgs gsr pfhqx pfhqx cmdgs pga
rpyf jejc adaiou dutv imbenyu dqw zhebjhu pryf vtxs yprf
cxj roprjn rqoh qacagru snxd
rczvi hfpl luc yowgj nvavlhw vjudkmv dwu teq
klwc cktzh ksnvswl nsgeu xyohp mhs fxnjhm fwrcg rdeadkx cim
ounvb vzqje ujctzzk iyy vxck ebtvbqr uswsmcr jveqz qejzv jmi pboq
lwffygh mqsh vnnj ufz qhms gqfuxo lurzmu
buf psdluck gapwoo wgll sbfavbc lljfvzx cdgo rpt sfvabcb
svefr kubbri fervs nboi zkvq
jwr vtc zkcpzb kczbzp cdned pzbzkc wigjuak fszgweu odflfek
vwdqm khnnj plokjg vnce venc vecn yzxtgb
tawl yrhoz tawl yrhoz
vvehsl kdhzgme rix rcs btm pxnlsps vlhesv sxpnslp yqjtool
eqpyw kpmkcyw wqhglxg ajfzo hbd qvmhy nhokah iisqvad kxuyd fxek
jsz txhwhah hxt djnvl srylveu pxp dzmmn epek tzs
joyzql jqczueb rtdyw fyc fjirfyn tjcalz joyzql fyc
pjrmiz xwnmwns kcqjuut zfgxhdr octwn kqppg zhfgxrd wmwnnxs
ema yqxqs aljjo ajloj wozb
urgmhiz epqj vhhaxdm ptlsvig qzbmm cumbho lkg gyzmg eaopyzf ncfy mqe
ijvwvo oszkees ugvyk hjdj ftip itfp
ylfw qutzdj mgqp cyjss yzsdqqi iykvs fyor sthyqp mrjtzee hgo zwqbtgk
bkfkns gco bykzc mje dwmkrwt ljegqor yxjxp oaleuu
xeltq ggyqis aud frtyxhx iwz wiz fwoxz fozxw
zdu nwduqsa nced iphaaxo
bqjj oah ezd brhgxrc pmkz kdog exw
ihatt hck iepn egemprp wrz wzcuo xjzeaa wku ivjvihh
cwkuof bmj qmxd qbtms zgdei bsqmt ssndhw eeenku lcsqy bvvodr
tek zsgytci vgoun kwwu
jcxvp ijxc buqgix uil zfoku
ggndshq bmjeo yqaxtik blspz yofh edaroy
ipvtxh ouye elln dllvx iqza nhwf zyfw pvlky
iydcx gvarm gvarm wegmiy
sfjd liiflle mulboe qywzs tzbns trojl pad mnfcrhb sltb
gthqj jvpsof jwlfyeg jwhlfj
qckv umzrge gnzc mnr xde
gvgxmhv txnait taxint ius iboqdj
vsfex kbpvsby qembkb efxvs vhflzvm eaazg dyg bbmekq
wxpfk xwfpk xwkpf cjsyi
knzg eefq feqe seppop ttxz qnqfn atgsy cch mkjlbwt uyhct
quzw jbiw miqehe qvf jyipqh kzcjxyh
teuvzf tdtwoi pcuafa cwgjk ccur lgmqv jpjdkk efrnw uloqn dpkjkj lwloeph
yaffjy xntstsv gygq sxttvsn tvnstxs
cvbmdf pfrfkna wupv van iocb hsiyke obspj ytyfkl hbsqtij hkcw
oeddmnu koso mdodeun ybe mhjbmwy ubejz soko yxvuv
nylhy ylnyh olb vcdik
gsp ilba llnu jjk urbvuma qzypf bkceotg ezxq hyvjngf
tfnegyq rue waeif tfnegyq mvqm
wvgnsk cpd oib wrdfaz kohwgkc kzzig hogkwck gkizz
fecuuyp yfq bvanvxb cjeqwf unw dccr qzh zqu voakj
utoazh bjuq kmhcre izmny mirorsy twnl jyoc
fnnpd dmr ccgu eqgewc zuqivf
kkxiba qdabuen oikaz dnuywmm
aogud adugo uzcglpj lucv dgoua mdsqa mvrg
lymhv sof hvyml mlvhy nit
chu bwxp xpbw ghaix seklnc ola zofnrwt uch
wtt abob vblijtd oabb qjws
uozrpw kgf gxidxm uehdr fta pqakkrq atf fat woaolk
gaee voshd ghlyy emvzlkg cmcgk tuwlsj jwtsul znrta mjieqph glker
qiugxas gkg cbzmoz kahs obzzcm
puz omcokz gjc heuqb
dgndhb wid wdi scwnrjf juaisgo eivaw hgdndb
mgcrd hnqg pkpeb vprxcp
atlcnzp fyp cpkivxi bzj ypf cqpt bysu
pnd jiitmzs csw mxnpck vxutdrs ivipzy cws xiegsy qut
txlk avcvbuu hnq yyriq ajyswd urgiwc
qgiqut gvblizs giqnfrk tty mvoj wpikl giqnfrk bkdpndu xztmxn hsmqxf
llthg zjslki wilj rcyfois bavz hrqxn
ytbw hlkl vip skycogy ejiirhx
ndmtg bthlbw lsoq cvlvo sqol sqlo bppl sdkbls dtpyzrq vgm
psm xpj xjp lqi spm gqirw aglpj
htg fcchvyt xffev szdu lieadft
nbjo qohgzu vofg vvild dbtyi pdolxn plnoao jxze xlpbxj brajzg
urpp jjv lihmvp ivkwdqr sesyp ypbry qok sesyp ivkwdqr was
yinepzv qvnzdtf apv ucxo bdioo juga hjfsyl hmowo avc
dmiv tplae iiuiaxx tpale pyzkc
giwhst mpexd byfyc swuzkc
yydkwp xuu vjya kav ujmcxy qrtp zvlk
lsvdyn tkw qxu omvlc wwmfvov mrgcoov dhpu tfair hupd zbx njzgwtw
zuz rsxc xsrc gdwwf nycsv zzu kcu
unlvzv jerqqgm nozma ykbflj qihqkx
pctffo begf ivrvy ezru mvqt waocq
tubtuk gxkc ikgw bjrird kxjebbh sbjyc yafkd khqajmt aclpmf gqfo yrpf
rdt vrxa fyudo myeosb ursflwk
wbjras edlbwdp ctobtw jbvtvcd xjgoo cmunxm mjtbpi klovx bypmsab unc
xckml uztr htublq vilabvr jdiwus qejxur evfw qqm
tzqq tzqq wkb wkb
dgmg ljzc dgmg mbmco cgze qsap jccvot uors iiq
rwvac woylk dmn teorprx nyuvz hcwwxlj lvej drbjo asjgq
ljen tpfl vixcivr guaf lnje waim jlen
djgaa janhi adudm yzv zkcb xqw fgvrz
kpkjoon ggzx skp rqcsw xgzg zgxg jtf ghc
rtnyxo qixfd nphekk mouzk gny fpzquw qgywx rpr gqydze
gawdlv vrivoof rte iyp gaih sfzplm
csojx wzojode uzy qulr lylmb guvtkwv
ovxj aamms ftxo ebckdqw wqvsdci jwfqxks jafrcrn yyomrot
qnu jqwr ywudxk qpsez rdc kiyfz iiecf dthxjjb bown
typ zxcvjo rip acjhl paaab qhqipg xkguye sbxy pomkvn
ofvaegv hgak oafevgv hkemar rqkha grklnsp msvkkku rekahm bxmjnw
ahoihju sdyn phi uhz lupbx
lavt jef klmq oqyfpf kis nazul ymezxek xpla fxyrfnt
nwnagwy hvpjqfg sgm ungfstr gso owqqxjh
hey hye ipyrt qxmthg jth wpbr hxgmtq cvfkfux qykdzhk movcfnl vxyoc
zsras abnrj fgaczuk ssazr xzf cnxu gns wnqqy dwjh szars
uhb zanlvh lvdotkb xekl kcofo
lhx iccy ibkjw ciykxaj imsx ehamqlz iwzapxc rhaltv
pofit owmpqej vwrobh jvox gdqehss yyxd styu tfkm fiotp
ecz mdpoqsv mdpoqsv yxx rexok hcfll yvury hdhcfu juhkvpt rspnfj hxvgdir
ohed mtigaoe eodh agmiteo
vjvv hfco cppbxtw hawsjxz ovlsq qgs risgwhg auhj
togivgg czrtvw ccz wzvtrc bse lsk
ndc ndc lrfi iyleol nchx jxpv xdcsfmp nnx wtvq pih tgc
hzpf sur zhfp klfmhx lbuidp xiqimnf
qddpdk trfxpip pnsowj hidgvnf prur rsrautp aamykfm fysqjmq xwzjane mbmtxhf oqctt
lfd eops govslp ultbye vrqai hcjkcf snpape
cbok koumkad otpozb pqcs emilpe wpcyvxd bock
spjb xkkak anuvk ejoklh nyerw bsjp zxuq vcwitnd xxtjmjg zfgq xkpf
juo pmiyoh xxk myphio ogfyf dovlmwm moevao qqxidn
"""

#DAY3INPUT = 265149
DAY3INPUT = 12

DAY2INPUT = """5806	6444	1281	38	267	1835	223	4912	5995	230	4395	2986	6048	4719	216	1201
74	127	226	84	174	280	94	159	198	305	124	106	205	99	177	294
1332	52	54	655	56	170	843	707	1273	1163	89	23	43	1300	1383	1229
5653	236	1944	3807	5356	246	222	1999	4872	206	5265	5397	5220	5538	286	917
3512	3132	2826	3664	2814	549	3408	3384	142	120	160	114	1395	2074	1816	2357
100	2000	112	103	2122	113	92	522	1650	929	1281	2286	2259	1068	1089	651
646	490	297	60	424	234	48	491	245	523	229	189	174	627	441	598
2321	555	2413	2378	157	27	194	2512	117	140	2287	277	2635	1374	1496	1698
101	1177	104	89	542	2033	1724	1197	474	1041	1803	770	87	1869	1183	553
1393	92	105	1395	1000	85	391	1360	1529	1367	1063	688	642	102	999	638
4627	223	188	5529	2406	4980	2384	2024	4610	279	249	2331	4660	4350	3264	242
769	779	502	75	1105	53	55	931	1056	1195	65	292	1234	1164	678	1032
2554	75	4406	484	2285	226	5666	245	4972	3739	5185	1543	230	236	3621	5387
826	4028	4274	163	5303	4610	145	5779	157	4994	5053	186	5060	3082	2186	4882
588	345	67	286	743	54	802	776	29	44	107	63	303	372	41	810
128	2088	3422	111	3312	740	3024	1946	920	131	112	477	3386	2392	1108	2741
"""
DAY1INPUT = "9513446799636685297929646689682997114316733445451534532351778534251427172168183621874641711534917291674333857423799375512628489423332297538215855176592633692631974822259161766238385922277893623911332569448978771948316155868781496698895492971356383996932885518732997624253678694279666572149831616312497994856288871586777793459926952491318336997159553714584541897294117487641872629796825583725975692264125865827534677223541484795877371955124463989228886498682421539667224963783616245646832154384756663251487668681425754536722827563651327524674183443696227523828832466473538347472991998913211857749878157579176457395375632995576569388455888156465451723693767887681392547189273391948632726499868313747261828186732986628365773728583387184112323696592536446536231376615949825166773536471531487969852535699774113163667286537193767515119362865141925612849443983484245268194842563154567638354645735331855896155142741664246715666899824364722914296492444672653852387389477634257768229772399416521198625393426443499223611843766134883441223328256883497423324753229392393974622181429913535973327323952241674979677481518733692544535323219895684629719868384266425386835539719237716339198485163916562434854579365958111931354576991558771236977242668756782139961638347251644828724786827751748399123668854393894787851872256667336215726674348886747128237416273154988619267824361227888751562445622387695218161341884756795223464751862965655559143779425283154533252573949165492138175581615176611845489857169132936848668646319955661492488428427435269169173654812114842568381636982389224236455633316898178163297452453296667661849622174541778669494388167451186352488555379581934999276412919598411422973399319799937518713422398874326665375216437246445791623283898584648278989674418242112957668397484671119761553847275799873495363759266296477844157237423239163559391553961176475377151369399646747881452252547741718734949967752564774161341784833521492494243662658471121369649641815562327698395293573991648351369767162642763475561544795982183714447737149239846151871434656618825566387329765118727515699213962477996399781652131918996434125559698427945714572488376342126989157872118279163127742349"

def day7_CalculateWeight(tabProgs, indexFather):
    indexSon = []

    for son in xrange(2, len(tabProgs[indexFather])):
        for index in xrange(0, len(tabProgs)):
            if tabProgs[index][0] == tabProgs[indexFather][son]:
                indexSon.append(index)

    for index in indexSon:
        tabProgs[indexFather][1] = tabProgs[indexFather][1] + day7_CalculateWeight(tabProgs, index)

    return tabProgs[indexFather][1]

def day7_CheckWeight(tabProgs, indexFather):
    indexSon = []

    for son in xrange(2, len(tabProgs[indexFather])):
        for index in xrange(0, len(tabProgs)):
            if tabProgs[index][0] == tabProgs[indexFather][son]:
                indexSon.append(index)
    for index in xrange(1, len(indexSon)):
        if tabProgs[indexSon[index]][1] != tabProgs[indexSon[0]][1]:
            for index_ in indexSon:
                print tabProgs[index_][0:2],
            print
            for index_ in indexSon:
                print DAY7INPUT.splitlines()[index_].split(' ')[0:2],
            print
            break

    for index in indexSon:
        day7_CheckWeight(tabProgs, index)

def day7_():
    tabProgs = []
    nameTop = day7()
    for prog in DAY7INPUT.splitlines():
        tabProg = []
        for data in prog.split(' '):
            tabProg.append(data)
        if len(tabProg) > 2:
            del tabProg[2]

        tabProg[1] = int(tabProg[1][1:-1])

        for index in xrange(2, len(tabProg)-1):
            tabProg[index] = tabProg[index][:-1]

        if tabProg[0] == nameTop:
            indexTop = DAY7INPUT.splitlines().index(prog)

        tabProgs.append(list(tabProg))

    day7_CalculateWeight(tabProgs, indexTop)
    day7_CheckWeight(tabProgs, indexTop)



def day7():
    tabProgs = []
    for prog in DAY7INPUT.splitlines():
        tabProg = []
        for data in prog.split(' '):
            tabProg.append(data)
        if len(tabProg) > 2:
            del tabProg[2]

        tabProg[1] = int(tabProg[1][1:-1])

        for index in xrange(2, len(tabProg)-1):
            tabProg[index] = tabProg[index][:-1]

        tabProgs.append(list(tabProg))

    prog = 0
    while prog < len(tabProgs):
        if len(tabProgs[prog]) == 2:
            del tabProgs[prog]
        else:
            prog = prog + 1

    name = tabProgs[0][0]
    while True:
        newName = ""
        for prog in tabProgs:
            if name in prog:
                if name != prog[0]:
                    newName = prog[0]
                    break
        if newName == "":
            return name
        else:
            name = newName


def day6_():
    rayInput = DAY5INPUT
    input = []
    inputSow = []
    for number in rayInput.split('\t'):
        input.append(int(number))
    cycle = 0    
    
    while True:
        cycle = cycle + 1
        if input in inputSow:
            return cycle - 1 - inputSow.index(input)
        inputSow.append(list(input))

        maxi = max(input)
        indexMaxi = input.index(maxi)
        for number in xrange(0, min(maxi + 1, len(input))):
            index = (indexMaxi + number) % len(input)
            if input[index] == maxi:
                input[index] = input[index] - min(maxi, len(input) - 1)
                maxi = sys.maxint
            else:
                input[index] = input[index] + 1


def day6():
    rayInput = DAY5INPUT
    input = []
    inputSow = []
    for number in rayInput.split('\t'):
        input.append(int(number))
    cycle = 0    
    
    while True:
        cycle = cycle + 1
        if input in inputSow:
            return cycle - 1
        inputSow.append(list(input))

        maxi = max(input)
        indexMaxi = input.index(maxi)
        for number in xrange(0, min(maxi + 1, len(input))):
            index = (indexMaxi + number) % len(input)
            if input[index] == maxi:
                input[index] = input[index] - min(maxi, len(input) - 1)
                maxi = sys.maxint
            else:
                input[index] = input[index] + 1


def day4_():
    tot = 0
    for line in DAY4INPUT.splitlines():
        tot = tot + 1
        words = line.split(' ')
        wordsChecked = []
        for wordRand in words:
            word = ''.join(sorted(wordRand))
            if word in wordsChecked:
                tot = tot - 1
                break
            else:
                wordsChecked.append(word)
    return tot

def day4():
    tot = 0
    for line in DAY4INPUT.splitlines():
        tot = tot + 1
        words = line.split(' ')
        wordsChecked = []
        for word in words:
            if word in wordsChecked:
                tot = tot - 1
                break
            else:
                wordsChecked.append(word)
    return tot

def day3_(): #not done
    DROITE      = 0
    HAUT        = 1
    GAUCHE      = 2
    BAS         = 3

    direction = DROITE
    width = 1
    while True:
        if width * width >= DAY3INPUT:
            break
        else:
            width = width + 2
#    width = width + 6
    matrix = [[0 for x in xrange(0, width)] for y in xrange(0, width)]
    x, y = width/2, width/2

    while True:
        matrix[x][y] = matrix[x+1][y] + matrix[x+1][y+1] + matrix[x-1][y+1] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x][y+1] + matrix[x-1][y] + matrix[x+1][y-1]
        if matrix[x][y] == 0:
            matrix[x][y] = 1
#        print matrix[x+1][y], matrix[x+1][y+1], matrix[x-1][y+1], matrix[x-1][y-1], matrix[x][y-1], matrix[x][y+1],  matrix[x-1][y], matrix[x+1][y-1]
#        print matrix[x][y], x, y
#        print " "
        if direction == DROITE:
            x = x + 1
            if matrix[x - 1][y + 1] == 0:
                direction = HAUT
                print "BAS"
        elif direction == HAUT:
            y = y + 1
            if matrix[x - 1][y + 1] == 0:
                direction = GAUCHE
                print "DROITE"
        elif direction == GAUCHE:
            x = x - 1
            if matrix[x - 1][y + 1] == 0:
                direction = BAS
                print "HAUT"
        else:
            y = y - 1
            if matrix[x - 1][y + 1] == 0:
                direction = DROITE
                print "GAUCHE"
        for i in matrix:
            for j in i:
                print j,
            print
        print x, y
        if matrix[x][y] > DAY3INPUT:
            return matrix[x][y]


def day3():
    width = 1
    num = DAY3INPUT
    while True:
        if width * width >= num:
            break
        else:
            width = width + 2
    squareCpt = width * width

    #"put" the number on the last line
    num = num + (3 - (num - (width - 2) * (width - 2))/ (width)) * (width - 1)
    #       hauteur        + largeur
    return (width - 1) / 2 + abs(squareCpt - (width - 1) / 2 - num)

def day2_():
    tot = 0
    oldTot = 0
    for line in DAY2INPUT.splitlines():
        numbers = line.split('\t')
        for i in xrange(0, len(numbers)):
            for j in xrange(i + 1, len(numbers)):
                n1 = int(numbers[i])
                n2 = int(numbers[j])
                if n1 % n2 == 0:
                    tot = tot + (n1 / n2)
                    break
                if n2 % n1 == 0:
                    tot = tot + (n2 / n1)
                    break
            if oldTot <> tot:
                oldTot = tot
                break
    return tot

def day2():
    tot = 0
    for line in DAY2INPUT.splitlines():
        max = 0
        min = sys.maxint
        for number in line.split('\t'):
            if max < int(number):
                max = int(number)
            if min > int(number):
                min = int(number)
        tot = tot + (max - min)
    return tot

def day1_():
    tot = 0
    lenCap = len(DAY1INPUT)
    haslfLenCap = lenCap/2
    for i in xrange(0, len(DAY1INPUT) - 1):
        if DAY1INPUT[i] == DAY1INPUT[(i+haslfLenCap)%lenCap]:
            tot = tot + int(DAY1INPUT[i])

    return tot

def day1():
    tot = 0
    for i in xrange(0, len(DAY1INPUT) - 1):
        if DAY1INPUT[i] == DAY1INPUT[i+1]:
            tot = tot + int(DAY1INPUT[i])

    if DAY1INPUT[0] == DAY1INPUT[len(DAY1INPUT) - 1]:
        tot = tot + int(DAY1INPUT[0])

    return tot

print day7_()
