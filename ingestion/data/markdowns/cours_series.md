Cours MP  chapitre 1 : les séries numériques.

Généralités

I.
La partie I aborde les séries dans un espace vectoriel de dimension finie.
1) Définition
Soit E un espace vectoriel de dimension finie. Soit u une suite de terme général un  E, on appelle série associée
la suite des sommes partielles (Sp)pIN avec

Sp =

. On parle de la série de terme général un.

Notation : on parle de la série

2)  Définition
On dit que la série est convergente si la suite des sommes partielles est convergente. Dans les autres cas, on dit
que la série est divergente.

En cas de convergence, la limite S =

est appelée somme de la série. On la note

La quantité Rp =

est alors appelée reste d'ordre p de la série.

La convergence d'une suite ou d'une série d'éléments d'un espace vectoriel s'exprime en fonction de la norme
choisie. On garde en mémoire que dans un espace de dimension finie, toutes les normes sont équivalentes.

3) Exemples
Ces premiers exemples sont pris dans IR,

a) La série de terme général

est convergente.

On pose un =

pour n  1 ,  Sn =

, les sommes partielles sont croissantes car les termes sont positifs.

C'est l'occasion de rappeler qu'une suite réelle monotone (dans ce cas croissante) n'a que deux comportements
possibles:


Ici les sommes partielles sont majorées, en effet, deux méthodes élémentaires possibles:

croissante et majorée et dans ce cas converge,
croissante et non majorée et dans ce cas diverge vers +.

-  montrer que  n > 1,  Sn   2 –

 par récurrence.

-  montrer que  k  2

 , puis

, séparer en deux sommes et changement

d'indice, on en déduit une majoration de Sn.

Ces deux méthodes ne nous donnent pas la limite  de la série de terme général

, on sait seulement que la

limite  est  2.

b) La série harmonique de terme général

 est divergente

un =

 pour n  1, donc Sn =

, la suite des sommes partielles est croissante.

Deux techniques pour montrer que la série est divergente:

1

p0kkupup0kkpulim0kkup0kkuS2n12n1n1k2k1n1)1k(k1k12k11k1)1k(k12n1n1n111kkn

-

Si on suppose que (Sn) converge, alors comme suite extraite, (S2n) a même limite, mais par différence:

S2n – Sn =

 ne peut tendre vers 0.

-  Montrer que les suites un =Sn – ln(n) et vn = Sn – ln(n+1) sont adjacentes. On en déduit qu'elles ont même

limite et par la même occasion, on prouve que Sn ~ ln(n) donc Sn   + si n  +.

Dans ce cas, on ne peut pas définir le reste d'ordre n.

4) Proposition
On ne modifie pas la nature d'une série (convergente, divergente) en modifiant un nombre fini de termes de la
suite.

5) a) Proposition
Soit une série de terme général un  E,
Si la série converge, alors le terme général un tend vers 0.

dém : un = Sn – Sn-1 et les deux sommes partielles ont même limite en cas de convergence de la série.

b) Corollaire
Si le terme général ne tend pas vers 0, la série ne converge pas.

 Attention

C'est une condition nécessaire mais pas suffisante, par exemple

 tend vers 0, mais la série harmonique diverge.

6) Proposition
Comme les séries ne sont que les sommes partielles des suites dans un espace vectoriel de dimension finie, les
structures algébriques vues en MPSI sont conservées:
Les séries vectorielles convergentes ont une structure d'espace vectoriel sur E (IK espace vectoriel).
Soit deux séries vectorielles de terme général un et vn convergentes avec pour sommes respectives S et S',
(, )  IK2  la série de terme général wn = un + vn est convergente, de somme S + S'.

7) Théorème fondamental d'équivalence suite/série
Soit une série quelconque, de terme général un. On retrouve ce terme général à partir de Sn – Sn-1 = un pour n  1.
Ceci définit une bijection entre les séries et les suites.
Soit (un)  EIN une suite vectorielle, la suite (un) converge dans E si et seulement si la série
convergente.
démonstration :

est

posons Tn =

= un+1-u0

La convergence de la série

n'est rien d'autre que la convergence de la suite (Tn). Si la série

converge, alors (un+1) converge. Et réciproquement, si (un) converge, la suite (Tn) converge.

Il y a deux façons classiques d'exploiter ce résultat :

soit on exprime un comme une somme partielle à partir de un =

Soit en cas de convergence de la série

, on a également  - un =

, où  est la limite de

la suite (un).

8) Convergence Absolue
Dans l'étude de la convergence d'une série ou d'une suite, deux situations sont à distinguer :

2

21n21.nk1n21nkn1)uu(nn1nkkkuu01)uu(nn1)uu(nn10101uuunkkk)uu(nn1nkkkuu1



on connaît ou on identifie la limite éventuelle  de la suite ou de la série. Dans ce cas, on peut poser

et étudier la norme de la différence.

  On ne connait pas la limite , et il ne reste comme ressource que l'étude de la contribution de chaque
terme un dans la somme partielle. Donc on envisage essentiellement la norme N(un) de ce terme.

Définition

Soit E un espace vectoriel de dimension finie muni d'une norme N, soit

une série vectorielle. On dit

que la série

converge absolument si la série NUMERIQUE

est une série convergente. C'est

une série de réels positifs ou nuls.

Théorème
Soit E un espace de dimension finie, la convergence absolue d'une série de E implique la convergence.

Démonstration:
On revient d'abord au cas réel en considérant une norme particulière sur E. Soit B=(e1,…,ep) une base

quelconque de E, on pose N(x) = sup{|xi|/i [1..p]} où

(N est la norme infinie).

Pour tout vecteur un on pose

. La convergence absolue de

est équivalente à la

convergence absolue des p séries numériques

. La convergence de la série

est équivalente à

la convergence des p séries numériques

. Il reste à prouver que la convergence absolue d'une série

dans IR implique la convergence.

Proposition

Soit

une série numérique réelle absolument convergente, alors la série

converge;

Démonstration

On pose Sn =

, d'abord la suite (Sn) est bornée. En effet

pour =1, n0  IN, n  IN, n>n0 

 comme reste partiel d'une série absolument convergente.

Donc

, il en résulte que la suite (Sn) est bornée dans IR.

D'après le théorème de Bolzano Weierstrass, elle admet au moins une valeur d'adhérence .
 est limite d'une suite extraite (S(k)) .
Supposons que (Sn) ne converge pas vers  :
>0, n0  IN,  n1  IN, n1>n0 et

  (1)

Or pour >0 fixé, n0  IN, (n,n1)  IN2, n>n0 et n1>n0   



  (2)

3

nkku0nunu)u(Nnpiiiexx1piii,nneuu1)u(Nnni,nununi,nunununkku010nnkku1100nnkknnuSS1nSnnkku121nnSS

On fixe n0 conformément à (2), on choisit n1 conformément à (1), et pour tout n=(k)>n0, il en résulte que

, ce qui est une contradiction.

Attention, la convergence n'implique pas la convergence absolue !

La série harmonique alternée

 converge , sa somme vaut ln(2)

Une technique de base sur ce classique est la suivante:

On pose Sn =

,

S2n =

=

=

=

On peut alors utiliser une somme de Riemann:

 =



Enfin S2n+1 = S2n –1/(2n+1)  les suites extraites de rang pair et impair des sommes partielles convergent vers la
même limite, donc la série converge et a pour limite ln(2).

Or la série

 ne converge pas absolument puisque

 diverge.

II Cadre des séries numériques : Les séries de référence.

1)  Les séries géométriques
Théorème
Soit q  IR, on définit un = qn , la série de terme général un converge si et seulement si |q| < 1.

Dém :

La somme partielle se calcule : Sn =

 pour q  1

Donc en cas de convergence



2)  Les séries de Riemann
a)  Définition

Soit   IR , on appelle série de Riemann, la série de terme général

  , pour n > 0.

b)  Exemples :

les séries vues en exemple ci dessus sont des cas particuliers de séries de Riemann.

c)  Théorème

 converge   > 1

Démonstration
Nous allons comparer la série à une intégrale, c'est une technique très importante dans ce chapitre.

4

2nSnn1n)1(n0kk1k)1(1n0pn0p2p211p211n0p1n21p2p212p11n0p1n21p1p1p11n21npp11n21npp11n1k1n1knk11n1kn110)2ln(t1dtnn1n)1(n1n1q1q11n0knuq11n1n1

D'abord, on peut remarquer pour   0 , d'une manière très élémentaire

 ne tend pas vers 0, donc la série ne

peut converger. Ensuite on a une série à termes positifs, la convergence est donc équivalente à la majoration des
sommes partielles.

Ensuite pour  > 0, on a f : t 

 est une fonction décroissante sur IR+*.

Donc par encadrement  t  [k,k+1] , avec k  1   :

,

on intègre l'inégalité:

on somme les inégalités en utilisant Chasles:

Dans la somme de droite, on fait un changement d'indice:

Enfin on bascule l'encadrement:

Maintenant, la forme de la fonction permet de calculer une primitive:

Si  = 1 ,

 

 donc la série diverge.

Si   1,

deux sous cas,

Si 0 <  < 1,

 + et la série diverge.

Si  > 1,

 

 et le terme de gauche a une limite en + ,

c'est donc une suite bornée, donc majorée. La somme partielle est donc majorée et converge.

d)  Comportement du reste

Théorème

Pour une série de Riemann de terme général

, lorsque  > 1  ,  Rn ~

Démonstration
Une façon d'encadrer le reste est de produire le même encadrement mais avec un deuxième indice:
d'après la définition du reste :

Rn =

, on pose donc Rn(p) =

 et on encadre l'expression en considérant n fixé et p > n:

C'est la même fonction que précédemment qui est utilisée:

 conduit à :

les deux intégrales se calculent et n'oublions pas que n est fixé, p  +

par exemple

 

si on passe à la limite, par théorème d'encadrement:

5

n1t1)1k(1t1k1)1k(1dtt1k11kkn1k1n1n1k)1k(1dtt1k11n2k1n1n1kk1dtt1k1dtt1k1dtt111n1n1kn1)nln(dtt1n1)1nln(k1)nln(1n1k]1n[11]t[11dtt11n11n1]1)1n[(11dtt1k111n1n1kn1kn1k1dtt11n1k1k1]1n[111n11n1p1nkpk1limp1nkk1p1nk1p1np1nk)1k(1dtt1k1dtt1)p(Rdtt11p1nn2p2n])1p()1n[(11]t[11dtt1111p1n11p1n1)1n(11

 et désormais on peut prendre l'équivalent quand n  +

3)  La série exponentielle
Théorème

 x  IR  , la série de terme général un =

 converge et

Démonstration
On utilise la formule de Taylor avec reste intégral appliquée à la fonction exp.
Rappelons cette formule:
Pour f = exp de classe C sur IR,  x IR

f(x) = f(0) + xf’(0) + ….. +

soit

ex =

+

 or

on pose vn =

, pour x = 0 , il n'y a rien à faire, pour x  0 ,

Donc

 0 , ce qui signifie que pour n assez grand |vn+1|< |vn| ,

donc la suite v décroît et est minorée par 0, elle converge. Sa limite  est

nécessairement 0, sinon

 ce qui est contradictoire.

Nous avons donc majoré le reste intégral. La série exponentielle converge avec

 ex

III Cadre des séries numériques : les méthodes de comparaison
1)  Comparaison avec des séries à termes équivalents, négligeables ou dominants.
a) Théorème

Soit

et

 deux séries à termes POSITIFS,

on note Sn(u) le terme général de la série

(la somme partielle de la suite u) et Sn(v) celui de la série

. De même on note  Rn(u)  le reste d'ordre n de la série

si elle converge, et Rn(v)  le reste d'ordre n

de la série

 si elle converge.

On suppose   n  IN , 0  un  vn
Alors on a les résultats suivants
i)

converge 

converge et Rn(u)  Rn(v)

ii)

diverge 

diverge et Sn(u)  Sn(v)

Démonstration
C'est un encadrement sur les sommes partielles.

b) Corollaire
Les comparaisons entre une série étudiée et une série de référence peuvent se faire par l'intermédiaire des outils
de comparaison vus en Sup, parfois plus sophistiqués qu'une inégalité directe  : o , O et équivalents.

6

1n1)1n(11)p(R)2n(1111nn11~)1n(11~)p(R!nxnxnne!nxx0)1n(n)n(ndt)t(f!n)tx()0(f!nxn0kk!kxx0tndte!n)tx()!1n(x)esup(dte!n)tx(1n]x,0[tx0tn!nxn1nxvvn1n1nxvvn1n1vvn1nn0kk!kxnunvnunvnunvnvnununv

Soit

et

 deux séries à termes POSITIFS, avec les notations du théorème ci dessus:

i)

ii)

iii)

iv)

 un = O(vn) et

converge 

converge et Rn(u) = O(Rn(v))

un = o(vn) et

diverge 

diverge et Sn(u) =o(Sn(v))

un ~ vn et

un ~ vn et

converge 

converge et Rn(u) ~ Rn(v)

diverge 

diverge et Sn(u) ~ Sn(v)

C'est un point central de ce chapitre.

Démonstration
Tout d'abord, pour les comportements de même nature des deux suites, c'est un problème d'encadrement. Tous
les cas se traitent de la même manière.
Considérons par exemple le cas iii)
Comme un ~ vn , il existe un rang à partir duquel   un  2vn
Comme la série

converge par application du théorème a).

converge, la série

Pour la comparaison des restes, revenons à la définition de l'équivalence:
un ~ vn    > 0  n0  IN , k  IN , k > n0  vk(1 – )  uk  vk(1 + )
On somme ces inégalités pour n > n0 , il vient  Rn(v)(1 – )  Rn(u)  Rn(v)(1 + ) , ce qui traduit l'équivalence
des deux restes.
Noter que ces deux restes sont de limite nulle puisque les séries convergent.

Observons le cas iv) pour l'équivalence des sommes partielles. En effet, il se peut que les premiers termes des
deux suites soient très différents, mais la divergence des sommes partielles va assurer l'équivalence des
infiniment grands.
Donc supposons un ~ vn et

diverge,

  > 0  n0  IN , k  IN , k > n0  uk(1 – )  vk  uk(1 + )
On considère Sn(v) pour n > n0 , il vient par encadrement:

On fait apparaître Sn(u) :

Comme Sn(u)  + , il ne manque finalement qu'un nombre fini et fixe de termes à droite et à gauche. On
rassemble tout ce qui s'arrête à n0 :

pour n  + ,

  0 car le numérateur ne dépend pas de n, il en est de même pour la

majoration de droite.

Donc  N  IN , n > N  – <

 <  et –  <

< +

On rassemble ce qui vient d'être obtenu:

  > 0, N  IN ,  n IN  n > N 

 d'où

l'équivalence des sommes partielles.

7

nunvnvnununvnvnununvnv2nunun1nkkn0kkn0kkn1nkkn0kk0000u)1(vvu)1(v)u)u(S)(1(vv)u)u(S)(1(v0000n0kknn0kkn0kkn0kknn0kk)1()u(S)u)1(v)u(S)v(S)1()u(S)u)1(vnn0kkn0kknnnn0kkn0kk0000)u(S)u)1(vnn0kkn0kk00)u(S)u)1(vnn0kkn0kk00)u(S)u)1(vnn0kkn0kk00)21()u(S)v(S)21(nn

2) Exemples d'utilisation :
a) Critère de Riemann
Soit une série de terme général un positif, soit   IR tel que nun  a > 0
Si  > 1 ,

converge.

Si   1 ,

diverge.

On a également si nun  0 avec  > 0 , alors

converge.

Démonstration
On a une série équivalente à une série de Riemann.

b) Exemples:

Convergence et calcul de

;

3) Comparaison des séries à des intégrales
a) Théorème
Soit f une fonction continue par morceaux sur [0,+[  (on rappelle qu'une fonction continue par morceaux sur un
segment est intégrable sur ce segment), à valeurs dans IR+, et décroissante.

La série de terme général un =

est convergente.

Un petit dessin:

Démonstration :

*

 t  [k–1,k], f(k)  f(t)  f(k–1)  0 

 f(k–1) – f(k) , donc les termes de la série sont positifs

On somme ces inégalités :

 f(0) – f(n)  f(1) cqfd.

b) Corollaire

La série

converge  f intégrable sur IR+

On verra ce que signifie f intégrable sur IR+ dans le chapitre sur l'intégration sur un intervalle.
Dans notre progression il suffit de constater que les sommes partielles sont majorées par f(1) – f(n);

c) Application

8

nununu2n21n11241nnnn)n(ffn1n)k(ffk1kn1kkun)n(f

On utilise ce critère quand la série est définie par une fonction décroissante positive dont on peut (sait?) calculer
une primitive.

Par exemple: un =

, le critère de Riemann ne donne rien.

Or constate que f(x) =

 est décroissante et positive à partir de [2,+[

Or

=



 par valeurs inférieures. Donc la série est convergente.

Cette intégrale s'appelle une intégrale de Bertrand, on peut généraliser la méthode en remplaçant l'exposant deux
par un exposant quelconque, par contre l'intégration nécessite alors un changement de variables.

d) Remarque ultime
Retenez que pour une fonction décroissante, il est toujours fructueux de comparer une série de terme général f(n)
avec une intégrale de f, que la série converge ou non. La remarque s'applique également au reste d'ordre n.

4)  Critère de d'Alembert
a) Théorème

Soit

, une série à termes strictement positifs.

On suppose que

 tend vers   0 quand n  +.



0   < 1  

 converge.

   > 1 

diverge

   = 1 ne permet pas de conclure.

Démonstration
On place un réel q entre  et 1.

Dans le cas  < q < 1, on écrit q =

, comme

  < q , il existe un rang à partir duquel





, donc la suite de terme général

 est décroissante et positive, donc con verge et est bornée.

Ce qui signifie que un = O(qn) , or la série

 converge. Donc la série

également.

Dans le cas  > 1 , on place 1 < q  <  , comme

  > q , il existe un rang à partir duquel







, donc la série diverge par comparaison à la série de terme général qn qui

diverge trivialement.

b) Exemple

Nature de la série de terme général un =

5)  Formule de Stirling

Démonstration
C'est une application de la comparaison d'une série à une intégrale.
On pose un = ln(n!) = ln(1) + …+ ln(n), donc on va encadrer le terme ln(k) par :

9

2)n(lnn12)x(lnx1n22)x(lnxdxn2)tln(12ln1nnun1nuunnunnun1nqqn1nuun1nuun1nqqnn1n1nququnnqunqnnun1nuun1nuun1nqq00nn1n1nquququ00nnququnn!nnenn2~!n

 k  2,

 ln(k) 



 un 

, on a déjà un équivalent de un ~ nln(n)

On pose alors vn = un – (

)ln(n) + n et on montre que vn admet une limite finie.

Comme vu en remarque dans la première partie, il suffit de prouver que vn+1 – vn est le terme  général d'une série
convergente.

Or vn+1 – vn = 1–(n + )ln(1 –

) ~

 donc la série converge et (vn) admet une limite .

Donc exp(vn) admet une limite et on en déduit qu'il existe   IR /

La valeur de  se calcule avec les intégrales de Wallis:

I2n =

~

IV séries alternées

1)  a) Théorème
Dans C , la convergence absolue d'une série implique sa convergence.

Démonstration
C est un IR espace de dimension 2, donc le résultat sur les séries vectorielles . C'est à dire que toute suite de
Cauchy converge. (voir cours sur les espaces vectoriels normés).

b) Corollaire
L'étude d'une série

 complexe ou réelle de terme général de signe non constant peut être réalisée en

appliquant des critères sur les séries positives à la série

. On notera qu'on obtient dans ce cas des critères

de convergence, mais pas la somme de la série.

2)  Théorème sur les séries alternées
a)  Définition
Une série

est dite alternée si un est de la forme un = (–1)nan avec an > 0

b)  Exemple

c)  Théorème de convergence des Séries Alternées: critère spécial des séries alternées.

Soit

 une série alternée avec an > 0 , si le terme général an tend vers 0 en décroissant alors

converge.

De plus, dans ce cas, le reste d'ordre n est majoré en valeur absolue par le premier terme négligé an+1 .

Si on pose S =

,

= Rn alors  |Rn|  an+1.

Démonstration
Les sommes partielles extraites de rang pair et impair sont adjacentes:

10

k1kdt)tln(1kkdt)tln(n1dt)tln(1n2dt)tln(21n211n12n121nenn~!n2n2)!n(2.2)!n2(n4pupununn1n)1(nna)1(nna)1(nna)1(n0kkuS

S2n+2 – S2n = a2n+2 – a2n+1 < 0 donc (S2n) décroît. De même S2n+3 – S2n+1 = –a2n+3 + a2n+2 > 0  donc (S2n+1) croît.
Et S2n+1 – S2n = –a2n+1  0 .
Enfin d'après le théorème sur les suites adjacentes, si on appelle S la limite commune, on a l'encadrement:

S2n+1< S < S2n  |S–S2n| < |S2n – S2n+1| = a2n+1 et de même avec |S–S2n+1|

d)  Exemple

converge car

 tend vers 0 en décroissant, et sans connaître la limite on peut écrire:

|Rn | =



V Ensembles dénombrables
1) a)  Définition
Un ensemble I est dit dénombrable si et seulement si il est en bijection avec IN.

b) exemple
Z est dénombrable: on pose (2n) = n et (2n+1) = -n-1.  établit une bijection de IN sur Z .

c) Définition
Un ensemble I est fini ou dénombrable s'il est en bijection avec une partie de IN.

Cette définition rassemble simplement les cas finis et dénombrables.

Il faut maintenant passer de dénombrable sur le plan de la définition à une manière de dénombrer les éléments
d'un ensemble : c'est une caractérisation des ensembles dénombrables.
2) Proposition
Soit I un ensemble, I est fini ou dénombrable si et seulement si il existe une suite (Jn) de sous-ensembles finis,
croissante pour l'inclusion, telle que

Démonstration:
Si I est dénombrable, il existe une bijection  de IN sur I, c'est-à-dire que les éléments de I sont indexés par IN :
I = (IN), on pose xn = (n) et Jn ={xi, 0i≤n}. Les (Jn) forment la suite de sous-ensembles finis, croissante pour
l'inclusion telle que

.

Si I est fini, c'est plus simple, on pose Jn = I pour tout n.

Réciproquement, si

avec les (Jn ) suite croissante de sous-ensembles finis pour l'inclusion.

On définit  de la manière suivante.
Pour tous les élément x  J0, on indexe les éléments de 0 à card(J0) -1.
Pour tous les éléments x  J1\J0, on indexe les éléments de card(J0) à card(J1)-1.
Par récurrence, on suppose construit une indexation de 0 à card(Jn)-1 des éléments de Jn.
Comme l'ensemble Jn+1 est fini, l'ensemble Jn+1\Jn est fini (éventuellement vide), on indexe ses éléments de
card(Jn) à card(Jn+1)-1.
On vérifie aisément que tout élément x de I est indexé par ce procédé.
Ce procédé théorique permet de construire explicitement des bijections de IN sur un ensemble dénombrable.

Exemples

  Q est dénombrable , on considère Jn ={p/q / |p|+q ≤ n} n 1.

IN2 est dénombrable, on considère les ensembles Jn ={(p,q)  IN2 /p+qn}.

Corollaire
Tout sous ensemble d'un ensemble dénombrable est dénombrable.

11

nn1n)1(1n1nkk1k)1(2n1INnnJIINnnJIINnnJI

3) Proposition
Un produit fini d'ensembles dénombrables est dénombrable.

Démonstration
Par récurrence sur le nombre d'ensembles intervenant dans le produit. Si E et F sont dénombrables, on montre
essentiellement que EF est dénombrable. On introduit (Jn) et (Kn) deux suites croissantes exhaustives  pour
l'inclusion de sous-ensembles finis respectivement pour E et F.
Les parties Ln = EnFn sont croissantes pour l'inclusion et leur réunion est EF.

4) Proposition
IR n’est pas dénombrable.

Démonstration
Montrons que le segment [0,1] n’est pas dénombrable.
Supposons que [0,1] soit dénombrable.
Les élémenst de [0,1] sont donc indexables et forment une suite (xn).
Si x0 ≥1/2 , posons y0=0.
Si x0<1/2, posons y0=1.

Dans les deux cas, y0= 1-E(2x0). C'est-à-dire
Plus généralement, tout réel x de [0,1] admet une approximation par défaut en base 2, de la même manière qu’il
admet une approximation décimale :
En posant

, il vient immédiatement pour tout N :

, c'est la même formule d'encadrement d'un réel en approximation

décimale, mais obtenue en base 2.
On va construire la suite (yn) en examinant à chaque indice le n° terme de la décomposition en base 2 de
l’élément xn.
Nous venons de définir

. Posons

.

Considérons maintenant l’élément

, x[0,1].

Soit m son indice dans l’indexation des réels de [0,1], x=xm.
Il apparaît que

, ce qui est une contradiction.

VI Familles sommables de nombres complexes.
1) Famille sommable de nombres réels positifs.
Le procédé introduit ici sera revu dans le cas des intégrales généralisées.
Définition
Soit S = (ui)iI une famille de nombres réels positifs, I un ensemble dénombrable.
On dit que S est sommable s'il existe un majorant M>0 tel que :
 F  I, F fini, la somme partielle des éléments indexés  par F est majorée par M :

≤ M.

Dans ce cas,

est un ensemble majoré. On note

sa borne sup.

Lorsque S n'est pas sommable, on note  + sa somme :

= + .

Dans le cas d'une indexation par IN, nous retrouvons la situation des séries numériques à termes positifs.
Mais comme on vient de le voir, il existe des ensembles dénombrables où l'indexation par IN n'est pas évidente.
Une deuxième subtilité intervient, c'est la question de l'ordre de sommation et de la méthode de sommation :

12

0y02x)x2(E2)x2(E)x(an1nnNN0iiiN0iii22)x(ax2)x(a)x(a1y000)x(a1ynnn0iii2yx)x(a1)x(ammmmFiiufini F,IF/uFiiIiiuIiiu

2) Théorème de sommation par paquets
Soit (In)nIN une partition de I, et S = (ui)iI une famille de nombres réels positifs. La famille S est sommable si et
seulement si:
i) pour tout n  IN, la sous-famille

est elle-même sommable.

ii) La série

est une série convergente.

Dans ce cas,

=

.

Ce théorème répond aux deux questions : peut-on réordonner les termes, et procéder à des sommations
intermédiaires.
La démonstration est indiquée comme étant hors-programme.
Mais elle  n'est pas sans intérêt…

  Supposons S sommable, posons

=  sa somme.

i) n  IN, In  I, donc toute sommation sur un  sous-ensemble fini de In admet le même majorant . La famille

est donc également sommable.

ii)  p  IN,

est donc une somme finie de sommes finies, et on a là une somme partielle

croissante, et majorée toujours par le même . Donc (Sp) est une suite croissante majorée, donc convergente. On

vient de démontrer que la série

est une série convergente, et que sa somme vérifie :

≤ .

iii) Il reste à démontrer que sa somme est .

Soit >0, par caractérisation de la borne supérieure, il existe un ensemble fini F tel que :

Soit i  F, il existe un indice j tel que i  Ij. Comme F est un ensemble fini, il existe un entier n0 tel que

, il suffit en effet de prendre n0 supérieur au maximum des indices j précités.

Comme les ui son positifs ou nuls, on obtient :

La croissance des sommes partielles permet de conclure.



Si S n'est pas sommable, il se peut très bien que pour tout n  IN, la sous-famille

soit quand

même sommable. On peut par exemple considérer le cas où In={n}. Mais même si chaque sous famille

est sommable, on montre qua la série

diverge. En reprenant les éléments de démonstration

du cas précédent, soit H > 0, comme S n'est pas sommable, il existe F fini tel que

. Avec l'existence

d'un indice n0 tel que

, on obtient alors

3) Familles sommables de nombres complexes.

a) Définition
Soit S = (ui)iI une famille de nombres complexes, I un ensemble dénombrable.
On dit que S est sommable si la famille  (|ui|)iI est sommable.

13

nIii)u(nIiiuIiiu0nIiinuIiiunIii)u(p0nIiipnuSnIiiu0nIiinuFiiu0n0nnIF0n0n0nIiinFiiuSunIii)u(nIii)u(nIiiuHuFii0n0nnIF0nn0nIiiuH

Une famille sommable indexée par IN est une série absolument convergente.

b) Commentaire
A priori, même dans les paragraphes précédents, lorsque la famille (|ui|)iI est sommable comme famille de réels
positifs, on n'a pas proposé d'ordonnancement particulier de I dénombrable pour en calculer la somme. On a écrit
que toute partition de I conduit au même résultat pour calculer un groupement par paquets. Et on a fait la
remarque que deux indexations différentes de I peuvent être vues comme deux partitions différentes.
En effet, par exemple dans I= IN, on peut considérer la partition correspondante à In = {n}, et si  est une
bijection de IN sur lui-même, on peut considérer I'n={(n)}.
Ainsi, le théorème de sommations par paquets prouve en corollaire que toute sommations après permutation des
indices de I dénombrable, donne le même résultat pour une famille sommable de réels positifs.
Dans le cas d'une famille complexe sommable, on va prouver que la somme est invariante par permutation de
l'ensemble des indices. Ensuite on prouvera le théorème de sommation par paquets pour une famille complexe
sommable. Dans le cas complexe, ce théorème englobe l'invariance par permutation des indices, mais le
programme officiel précise que la démonstration de l'invariance de la somme par permutation des indices est non
exigible, mais au programme.

On va donc commencer par passer du caractère sommable au calcul effectif de la somme.

c) Théorème d'invariance par permutation des indices
Soit S = (ui)iI une famille de nombres complexes sommable où I est un ensemble dénombrable
Soit une suite (Jn) de sous-ensembles finis, croissante pour l'inclusion, telle que

On pose

On pose

, la suite

 converge dans C, et sa limite  ne dépend pas du choix de la suite (Jn).

Lemme de découpage
Soit S = (ui)iI une famille de nombres complexes sommable, alors en posant pour tout i : ui = xi + iyi, les
familles (xi)iI et (yi)iI sont sommables.
De plus, pour tout xi, on pose xi
+ - xi
que xi = xi
sommables, et

-) sont positives. Alors les familles (xi

. Le résultat est analogue pour la famille (yi)iI.

-  pour tout xi et les familles (xi

+ = xi si xi ≥ 0, et xi

+ = 0 si xi < 0 et xi

- = 0 si xi ≥ 0, xi

+) et (xi

+) et (xi

- = -xi si xi < 0, de sorte

-) sont

Démonstration
Comme |ui|≥ |xi|, on en déduit le caractère sommable de la famille (xi)iI, il en est de même pour
|xi|≥ xi
De plus pour la famille (xi

+ , et les autres cas également.

+), montrons que la limite de

ne dépend pas du choix de (Jn) :

 (xi

+)iI étant sommable, on pose + la borne supérieure de

, on a vu que >0  FI, F

fini, tel que

.

En choisissant n0 tel que

, il vient :

Finalement, pour toute suite croissante pour l'inclusion (Jn), il vient :

et on passe à la limite dans chaque somme.

14

INnnJInnJinJuSnJSIiiJuSlimnIiiIiiIiixxxnnJiiJx)x(Sfini F,IF/xFiiFiix0nJF)x(Sx0nJFiinnnnnJiJiiJiiJiiiJiiyyixxu

d) Théorème
Soit I un ensemble dénombrable, l'ensemble des familles de nombres complexes sommables indexées par I est
un C espace vectoriel. L'application qui à une famille sommable associe sa somme est linéaire.

Il reste le théorème de sommation par paquets pour les familles sommables complexes. La démonstration est
hors programme.

4) Théorème de sommation par paquets pour une famille complexe sommable.
Soit (In)nIN une partition de I, et S = (ui)iI une famille sommable de nombres complexes. Alors :

i) pour tout n  IN, la sous-famille

est elle-même sommable.

ii) La série

est une série convergente.

et

=

.

VII Le cas des familles indexées par IN2
1)  Série double
a) Définition
Soit u = (up,q)(p,q)ININ une famille de nombres réels ou complexes indexée par ININ. On appelle série double la
série indexée par le terme général up,q .
b) Théorème de sommation pour les séries doubles positives réelles.
Soit S=(up,q)(p,q)ININ une famille de nombres réels positifs,

La famille S est sommable si et seulement si  p  IN , la série

converge vers un réel

ap  , et si

converge.

Dans ce cas, on peut inverser l'ordre de sommation :

 q  IN , la série

converge également vers un réel bq et

 converge.

De plus

, les sommes sont égales.

On parle de sommation par tranche, on dit qu'en cas de convergence, on peut inverser l'ordre de sommation.
Ce théorème est la conséquence de la partition de I = INxIN en parties de la forme In = {n}xIN et du théorème de
sommation par paquets.

c) Exemple:

, on regarde d'abord en sommant par rapport à q pour avoir une série géométrique convergente, comme

p > 1, la raison est toujours inférieure strictement à 1.

=

, ceci est le terme général d'un série convergente d'après le critère de Riemann, on

décompose la fraction en éléments simples:

15

nIii)u(nIiiuIiiu0nIiinuqpquppappquqqb0qq0ppba1q,1pqp12q2qp11p1p1)1p(p1

 1

d) Théorème de sommation pour les séries doubles complexes.
Soit (up,q)(p,q)ININ une famille de nombres réels ou complexes, si la famille  (|up,q|)(p,q)ININ est
une famille sommable (c'est à dire que le théorème 3 s'applique à la famille des |upq| ) , alors on
a :

 p  IN , la série

converge vers un réel ap  , et

converge ,

de même,

q  IN , la série

converge également vers un réel bq et

 converge.

De plus

, les sommes sont égales.

2)  Produit de deux séries
a)  Définition

Soit

et

deux séries réelles ou complexes (série signifie indexées par IN), on appelle série produit la

On définit la série double par  wpq =upvq .

b)  Théorème

Soit

et

deux séries réelles ou complexes absolument convergentes, de sommes respectives S et T,

la série produit est une famille sommable. Sa somme est ST.

Démonstration
La famille (|wpq|) est sommable, puisqu'en considérant la partition de IN2 définie par Jn = {n}IN, on trouve une

somme partielle

, qui est le terme général d'une série convergente. Le théorème de sommation par

paquets appliqué à cette partition entraîne que la somme vaut ST.

c) Produit de Cauchy.
Dans le cas d'une série produit, on utilise une autre partition de INxIN souvent plus fructueuse.
On introduit la partition suivante : n IN, In = {(p,q)  INxIN/ p+q =n}.
Ceci correspond à une somme diagonale. La série construite a pour terme général :

zn défini par zn =

= u0vn + u1vn–1 + …+unv0

La série de terme général zn s'appelle produit de Cauchy des séries

et

Proposition

Si les séries

et

sont absolument convergentes de sommes respectives S et T, la série produit de

Cauchy

est absolument convergente, et sa somme vaut ST.

Exemple

considérons un =

et vn =

 pour x et y deux réels. Les deux séries sont absolument convergentes.

16

1p)1p(p1qpquppappquqqb0qq0ppbanunvnunv0kknvun0kknkvununvnunvnz!nxn!nyn

On constate que la définition de zn donne zn =

La série produit de Cauchy vérifie

= e(x+y) =(

=

)(

=

=

) = ex ey

Le problème majeur est de savoir comment sommer les termes, d'abord tous les indices p, puis tous les q ? ou
l'inverse, ou en parcourant les indices (p,q) selon une règle différente?

d) Et pour les séries non absolument convergentes ?
Les choses se compliquent dès qu'on n'a plus convergence absolue!
Dans la plupart des cas, la façon de sommer modifie le résultat.

Voici un exemple. Posons un = vn =

, le critère spécial des séries alternées s'applique, la

série

converge, notons S sa somme.

Pour la série double de terme général upvq =

, sommons d'abord les termes en fixant p , on

obtient

Donc

qui admet une limite quand Q tend vers l'infini:

Maintenant considérons une sommation en diagonale, produit de Cauchy:

on a wn =

or si on étudie x  (x+1)(n+1–x) sur [0,n], on constate que

, donc par sommation,

le terme général wn ne tend pas vers 0. La série produit ne converge pas…

17

n0kknkvun0kknk)!kn(!kyxn0kknkyxkn!n1n)yx(!n1kzkxky1n)1(nnu)1q)(1p()1(qpQ0qQ0qqpqpv)1p()1(vuS)1p()1(p2P0pQ0qqpQPS)vu(limlimN0nnqpqpvun0kn)k1n)(1k(1)1()12n()k1n)(1k(

