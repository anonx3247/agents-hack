# Chapitre 16: Arithmétique dans Z

## Autour de la division euclidienne

### Diviseurs et multiples

#### Définition *Diviseur*

Dire que $a$ divise $b$ ou que $b$ est un multiple de $a$ si:
$$
∃ k ∈ \mathbb{Z} / ak = b
$$

#### Exemples

- Les diviseurs de 25 sont: 1, 5, 25, -1, -5, -25
- 3 divise 0 car $0 = 3 \times 0$
- 0 ne divise pas 3 car $∀ k ∈ \mathbb{Z}, 0k \neq 3$
- 0 divise 0

#### Propriété

Soient $a, b ∈ \mathbb{Z}$ $a$ divise $b$ si et seulement si $b \mathbb{Z} ⊂ a \mathbb{Z}$

ou on note
$$
x \mathbb{Z} = \{xk / k ∈ \mathbb{Z} \}
$$ 

#### Preuve

" $\implies$ ": On suppose que $a$ divise $b$ donc il existe $d / ad = b$
Soit $x ∈ b\mathbb{Z}, ∃ k ∈ \mathbb{Z} / x = bk$ donc $x = adk ∈ a \mathbb{Z}$

" $\impliedby$ ": $b ∈ b\mathbb{Z} ⊂ a\mathbb{Z}$ 
Donc $∃ k ∈ \mathbb{Z} / b = ak$ 

Donc $a$ divise $b$

#### Propriété

Soient $a,b,u,v ∈ \mathbb{Z}$
SOit $d ∈ \mathbb{Z}$ 
Si $d$ divise $a$ et $b$ alors $d$ divise $au + bv$

#### Preuve
$$
∃ k_1, k_2 ∈ \mathbb{Z} / a = dk_1, b = dk_2
$$

$$
au + bv = udk_1 + vdk_2 = d(uk_1 + vk_2)
$$

#### Propriété

$a | b$ et $b | a$  si et seulement si $a  = \pm b$

On dit alors que $a$ et $b$ sont "associés".

#### Preuve
" $\implies$" :
$$
∃ k_1, k_2 ∈ \mathbb{Z} / b = k_1a, a = k_2b
$$

$$
a = k_1 k_2 a \iff k_1 k_2 = 1
$$

$$
k_2 ∈ \mathbb{Z}^{*} \iff k_2 = \pm 1
$$

Donc $a = \pm b$ 

" $\impliedby$ " :
Facile

### Division Euclidienne dans l'anneau $(\mathbb{Z}, +, \times)$

#### Théorème "Théorème de la division euclidienne dans $\mathbb{Z}$"

Soient $a, b ∈ \mathbb{Z} , b \neq 0$

Il existe un unique couple $(q,r) ∈ \mathbb{Z}^2$ vérifiant:
$$
a = bq +r
$$
$$
0 \le r < |b|
$$ 

$q$ s'apelle le quotient et $r$ le reste de la division euclidienne de $a$ par $b$.

#### Preuve

##### Unicité

Soient $(q, r) , (q', r')$ deux couples realisant la division euclidienne de $a$ par $b$   
$$
a = bq + r = bq' + r'
$$

On a donc:
$$
bq - bq' = r' - r
$$

or $0 \le r < |b|$ et $0 \le r' < |b|$  

$$
|b| \times |q - q'| = |r'-r| < |b|
$$
$$
|q - q'| < 1
$$

Donc $|q - q'| = 0 \iff q = q'$

Donc

$$
bq - bq' = r'-r
$$
$$
0 = r'-r
$$
$$
r = r'
$$

##### Existence

Dans le cas ou $b ∈ \mathbb{N}^{*}$

On pose $q = \lfloor\frac{a}{b} \rfloor$, $r = a - bq$ 

On a $\frac{a}{b} - 1 < q \le \frac{a}{b}$

$$
a - b < bq \le a
$$
$$
a - bq - b < 0 \le a - bq
$$
$$
r - b < 0 \le r
$$

Dans le cas ou $b ∈ \mathbb{Z} \backslash \mathbb{N}$

On aboutie a $0 < r' \le -b$ 

$q = - \lfloor \frac{-a}{b}\rfloor$ 

#### Théorème "Caractérisation des sous-groupes de $(\mathbb{Z}, +)$"

$G$ est un sous-groupe de $(\mathbb{Z}, +)$ si et seulement si

$$
∃ a ∈ \mathbb{N} / G = a\mathbb{Z}
$$

De plus $a$ est unique et $a = 0 \iff G = \{0\}$  

#### Preuve

##### Unicité

Supposons donné $a, a' ∈ \mathbb{N}/ G = a\mathbb{Z} = a'\mathbb{Z}$

Donc
$$
a\mathbb{Z} ⊂ a'\mathbb{Z} \implies a | a' \text{ et } a'\mathbb{Z} ⊂ a\mathbb{Z} \implies a' | a
$$
Donc 

$a = \pm a'$ or $a, a' ∈ \mathbb{N} \implies a = a'$  

#### Preuve
" $\impliedby$ " :
Montrons que $a\mathbb{Z}$ est un sous-groupe de $(\mathbb{Z}, +)$  

$$
a\mathbb{Z} ⊂ \mathbb{Z}, a\mathbb{Z} \neq \varnothing \text{ car } a ∈ a\mathbb{Z}
$$

Soient $x, y ∈ a\mathbb{Z}$ Montrons que $-x + y ∈ a\mathbb{Z}$

$-x +y$ est une combinaison linéaire et donc est un multiple de $a$ et appartient a $a\mathbb{Z}$.   

" $\implies$" :

On consière $G$ un sous-groupe de $(\mathbb{Z}, +)$

- Cas ou $G = \{0\}$
On prends $a = 0$ fonctionne

- Cas ou $\{0\} ⊂ G, \{0\} \neq G$
$∃ k \neq 0 / k ∈ G$ Quitte a remplacer $k$ par $-k$ (qui reste dans $G$ ), on peut supposer que $k ∈ \mathbb{N}^{*}$

On note alors $A = G \cap \mathbb{N}^{*}$ 

$A$ admet un minimum car $k ∈ A$ donc $A \neq \varnothing$ et par axiome de Peano, notons le $a$.    

Montrons que $G = a\mathbb{Z}$ 

#### Preuve
" $\supset$  " :
- Par récurrence montrons que $∀ k ∈ \mathbb{N}/ ak ∈ G$
- Vrai pour $k = 0$ car $0 ∈ G$
- On suppose $k ∈ \mathbb{N} / ak ∈ G$ on veut montrer que $a(k+1) ∈ G$
- $a = \text{min}(A) \iff a ∈ G$ et $ak ∈ G$ donc par stabilité du groupe par la somme $a + ak ∈ G$   


Soit $k ∈ \mathbb{Z}$
- si $k ∈ \mathbb{N}$ alors $a k ∈ G$
- sinon $-ak ∈ G$ donc par inverse $ak ∈ G$ 
- $∀ k ∈ \mathbb{Z}, ak ∈ G \iff a\mathbb{Z} ⊂ G$ 


" $⊂$  " :
Soit $g  ∈ G$, effectuons la division euclidienne de $g$ par $a$

$$
∃ q, r ∈ \mathbb{Z} / g = aq + r, 0 \le r < a \iff r = g - qa
$$

or $g ∈ G$ et $-qa ∈ a\mathbb{Z} ⊂ G$ donc $r ∈G$

Or $r  = 0$ car $r < a$  et $a = \text{min}(A)$ 

## PGCD d'un nombre fini d'entiers

### Existence du PGCD

#### Théorème

Soient $r \ge 2, r ∈ \mathbb{Z}$, et $a_1, a_2, \cdots, a_n$ des entiers non nuls.

Il existe un unique entier $d$ strictement positif telque $∀ a_i, d | a_i$, i ∈ [1,r]

Si $d'$ est un entier divisant touts les entiers $a_i / i ∈ [1, r]$

alors $d' | d$

$d$ s'apelle le PGCD des entiers $a_1, \cdots a_n$ et on note:
$$
d = \text{PGCD}(a_1, \cdots a_n)
$$
$$

d = \land_{i=0}^{n} a_i
$$

#### Preuve

##### Unicité

Soient $d, d'$ deux PGCD

- $d'$ est un PGCD donc divise tous les $(a_i)_{i ∈ [[1,r]]}$
- par symmetrie on a que $d | d'$ \iff $d = \pm d'$  or $d, d' ∈ \mathbb{N}^{*}$ donc $d = d'$  

##### Existence

Soit
$$
a_1\mathbb{Z} + \cdots a_r\mathbb{Z} = \sum_{k=0}^{r} a_k\mathbb{Z}
$$ 

$$
= \{ \sum_{k=0}^{n} a_k j_k / ∀ k ∈ [[0, n]], j_k ∈ \mathbb{Z} \}
$$

Par la caractérisation des sous-groupes 
$∃ d ∈ \mathbb{N} / \sum_{k=0}^{n} a_k \mathbb{Z} = d \mathbb{Z}$ 

$$
∃ i ∈ [[1, r]] / a_i \neq 0
$$ 

car $a_1 , \cdots a_n$ sont tous non nuls

or $a_i ∈ \sum_{k=0}^{n} a_k \mathbb{Z}$ donc $d ∈ \mathbb{N}^{*}$

$a_i \mathbb{Z} ⊂ \sum_{k=0}^{n} a_k\mathbb{Z}$ 

donc $d | a_i$

Soit un entier $d'$ divisant tous les $a_i$ pour $1 \le i < r$
Donc pour tout $1 < i <= r, a\mathbb{Z}, d'\mathbb{Z}$

Donc $d\mathbb{Z} = \sum_{k = 0}^{n} a_k \mathbb{Z} ⊂ d'\mathbb{Z}\iff d' | d$ 

#### Exemples

- $1 \land 3 = 1$ 
- $6 \land 2 \land 1 = 2$
- $6 \land 9 = 3$

### Propriétés du PGCD
#### Propriétés

- $\forall2 a,b ∈ \mathbb{Z}, (a \land b) \land c = a \land (b \land c)$ 
- $∀ a, b ∈ \mathbb{Z}, a \land b = b \land a$ 

#### Corollaire

Si $a$ et $b$ sont des entiers non nuls alors on peut poser $a'= \frac{a}{a \land b}$
& $b' = \frac{b}{ a \land b}$

#### Remarque 

- $\land$ est une loi de composition interne associative, commutative sur $\mathbb{Z}$ et possède un element neutre 0 sur $\mathbb{N}$
- De plus $\times$ est distributive par rapport a la loi $\land$ sur $\mathbb{N}$ 

### L'Algorithme d'Euclide

#### Propriété

SOient $a,b ∈ \mathbb{Z}, b \neq 0$ on note $q$ et $r$ le quotient et le reste de la division euclidienne de $a$ par $b$

On a $a \land b = b \land r$ 

#### Preuve (Méthode Classique en Éxercice)

$a = bq + r$ donc $a \land b | a$ et $a \land b  | b$ donc divise $a - bq = r$

Donc $a \land b | b \land r$ 

$b \land r | b$ et $b \land r | r$ donc $b \land r | bq + r = a$

donc $b \land r | a \land b$

Donc $a \land b = \pm b \land r$ or ils sont que positifs donc

$$
a \land b = b \land r
$$

#### Théorème

Soient $a, b ∈ \mathbb{Z}, b \neq 0$

On a $a \land b$ est egal au dernier reste non nul en effectuant des divisions euclidiennes successives. 

#### Exemple

calculons $27 \land 31$

$$
27 = 31 \times 0 + 27
$$
$$
31 = 27 \times 1 + 4
$$
$$
27 = 4 \times 6 + 3
$$
$$
4 = 3 \times 1 + 1
$$
$$
3 = 3 \times 1 + 0
$$
$$
27 \land 31 = 1
$$

#### Preuve
- Montrons dans un premier temps que l'algorithme termine
- On effectue les divisions euclidiennes successives:

##### Étape 1

$$
a = b \times q_1 + r_0
$$
$$
0 \le r_0 < |b|
$$

##### Étape 2

$$
b = r_0 \times q_2 + r_1
$$
$$
0 \le r_1 < |b|
$$

##### Étape 3

$$
r_0 = r_1 \times q_3 + r_2
$$
$$
0 \le r_2 < |b|
$$

##### Étape k

$$
r_{k-3} = r_{k-2} \times q_k + r_{k-1}
$$
$$
0 \le r_{k-1} < r_{k-2} 
$$

Montrons qu'il existe $k ∈ \mathbb{N} / r_k = 0$

Sinon il existe une suite $(r_k)_{k ∈ \mathbb{N}}$ strictement décroissante d'entiers naturels 

## Théorème de Bézout et de Gauss

### Entiers premiers entre eux deux a deux et dans leur ensemble

#### Définition *Entiers premiers entre eux*

Soient $a, b ∈ \mathbb{Z}$ on dit que $a$ et $b$ sont premiers entre eux si $a \land b = 1$

Soient $a_1, \cdots a_n ∈ \mathbb{Z}$

On dit que $a_1, \cdots a_n$ sont premiers entre eux dans leur ensemble si
$$
\land_{i=0}^{n} a_i = 1
$$ 

Soient $a_1, \cdots, a_n ∈ \mathbb{Z}$ On dit que $a_1, \cdots, a_n$ sont premiers entre eux deux-a deux si
$$
∀ 1 \le i\pm j \le n, a_i \land a_j = 1
$$  

#### Théorème

Si $a_1, \cdots, a_n ∈ \mathbb{Z}$ sont premiers entre eux 2 a 2 alors il le sont dans leur ensemble

### Théorème de Bézout

Soient $a_1, \cdots, a_n ∈ \mathbb{Z}$

Si on note $d = \land_{i=0}^{n} a_i$ alors il existe $k_1, \cdots, k_n ∈ \mathbb{Z}$ telque $d = k_1 a_1 + \cdots + k_n a_n$

#### Théorème "Théorème de Bézout"

Soient $a_1, \cdots, a_n ∈ \mathbb{Z}$, ils sont premiers entre eux dans leur ensemble

si et seulement si,

$$
∃ k_1, \cdots, k_n ∈ \mathbb{Z} / 1 = \sum_{i=1}^{n} k_i a_i = 1
$$

#### Preuve
#### Preuve
" $\implies$" :

Déja vu

" $\impliedby$ " :
Pour $1 \le i \le r$, $d | 1 \implies d | \sum_{i=1}^{n} k_i a_i$

Et donc $\land_{i=1}^{n} a_i = 1$    

### Théorème de Gauss

#### Théorème "Théorème de Gauss"

Soient $a, b, c ∈ \mathbb{Z}$

- Si $a | bc$ et $a \land b = 1$ alors $a | c$ 
- Si $a \land b = 1$ alors $ab | c$  

#### Preuve

Comme $a | bc$ alors $∃ k ∈ \mathbb{Z} / bc = ka$ et comme $a \land b = 1$ alors par le théorème de Bézout,
$$
∃ u, v ∈ \mathbb{Z} / au + bv = 1
$$   
$$
c = c \times (au + bv)
$$
$$
c = c au + cbv = cau + ckav = a (ckv + cu)
$$
Donc $a | c$

- Comme $a | c$ alors $∃ k_1 ∈ \mathbb{Z} / c = ak_1$
- Comme  $b | c$ alors $∃ k_2 ∈ \mathbb{Z} / c = bk_2$
- Comme $a \land b = 1$ et d'après Bézout on a
$$
∃ u, v ∈ \mathbb{Z} / au + bv = 1
$$ 

Donc
$$
c = c(au+bv)
$$
$$
= cau + cbv
$$
$$
= bk_2au + ak_1 bv
$$
$$
= ab(k_2 u + k_1 v) 
$$

Donc $ab | c$ 

## PPCM d'un nombre fini d'entiers

### Éxistence du PPCM

#### Théorème

Soient $n \ge 2, n ∈ \mathbb{Z}$ et $a_1, \cdots a_n ∈ \mathbb{Z} / ∀ i, a_i \neq 0$

Il existe un unique entier naturek strictement positif $m$ vérifiant

- $m$ est un multiple de tous les $a_i$ avec $1 \le i\le n$
- Si $m'$ est un multiple de tous les $a_i$ pour $1 \le i \le n$ alors $m'$ est un multiple de $m$

On note alors
$$
m = \text{PPCM}(a_1, \cdots, a_n)
$$
$$
m = \lor_{i=1}^{n} a_i
$$


#### Preuve

##### Unicité

Soient $m, m'$ deux PPCMs de $a_1, \cdots, a_n$

comme $m$ est un PPCM, $m'$ est un multiple de $m$

$m$ et $m'$ jouant des roles symmétriques, on a également que
$m$ est un multiple de $m'$ Donc $m = \pm m'$ donc $m = m'$ car $m, m' ∈ \mathbb{N}^{*}$.

##### Éxistence
$$
\bigcap_{i = 1}^{n} a_i\mathbb{Z}
$$
est un sous-groupe de $(\mathbb{Z}, +)$ donc

$$
∃ m ∈ \mathbb{Z} / \bigcap_{i=1}^{n} a_i \mathbb{Z} = m\mathbb{Z}
$$

Comme
$$
\prod_{i=1}^{n} a_i ∈ \bigcap_{i=1}^{n} a_i\mathbb{Z}
$$ 
Cet ensemble est donc pas égal a $\{0\}$ 

Donc $m ∈ \mathbb{N}^{*}$

- $∀ 1 \le i \le n, m\mathbb{Z} ⊂ a_i \mathbb{Z}$

Donc $a_i | m$ donc $m$ est un multiple de $a_i$

Soit $m'$ un multiple commun a tout les $a_i$ pour $1 \le i \le n$

Alors $a_i | m'$ et $m'\mathbb{Z} ⊂ a_i \mathbb{Z}$ et $m'\mathbb{Z} ⊂ m\mathbb{Z}$

Donc $m | m'$ et $m'$ est un multiple de $m$.   

#### Exemples
- $2 \lor 3 = 6$ 
- $6 \lor 4 = 12$
- $3 \lor 4 \lor 7$

Par convention si l'un des $a_i = 0$ alors on a PPCM = 0  

### Propriétés du PPCM

#### Propriété

- $∀ a, b, c ∈\mathbb{Z},$

$$
a \lor b \lor c = (a \lor b) \lor c = a \lor (b \lor c)
$$
$$
∀ a, b ∈ \mathbb{Z}, a \lor b = b \lor a
$$
$$
∀ a,b,m ∈ \mathbb{Z}, (ma) \lor (mb) = |m| \times (a \lor b)
$$

#### Remarque

Le PPCM est une loi de composition interne sur $\mathbb{Z}$ qui est
- associative
- commutative
- posédant un élement neutre et $\times$ est distributive par rapport a la loi PPCM sur $\mathbb{N}$

#### Théorème

$$
∀ a, b ∈ \mathbb{Z}, a \land b \times a \lor b = |ab|
$$

#### Preuve

- Si $a = 0$ ou $b = 0$ alors $a \lor b = 0$ et $ab = 0$ donc la formule est banale

- On suppose donc que $a, b \neq 0$

**Cas 1**: ou $a \land b = 1$

Montrons que $a \lor b = |a \times b|$

- $a \text{ et } b  | a \times b$ donc $a \lor b | a \times b$

Donc $∃ k, k' ∈ \mathbb{Z} / a \lor b = ak  = bk'$

Donc $ak = bk'$ et comme $a \land b = 1$ on a d'après Gauss, $a | k'$ donc
$$
∃ k'' ∈ \mathbb{Z} / k' = ak''
$$
Donc $a \lor b = b \times k' = b \times a \times k''$ donc $a \lor b$ est un multiple de $a \times b$   

Donc $a \lor b  = \pm ab \iff a \lor b = |ab|$ 

**Cas 2**: ou $a \land b \neq 1$

On pose donc $a' = \frac{a}{a \land b}, b' = \frac{b}{a \land b}$

Donc $a' \lor b' = |a' \times b'|$ d'après le cas 1

$$
\left(\frac{a}{ a \land b}\right) \lor \left(\frac{b}{a \land b}\right) = | \frac{ab}{(a \land b)^2} |
$$

Donc
$$
(a \land b) ^2 \times \left(\frac{a}{ a \land b}\right) \lor \left(\frac{b}{a \land b}\right) = |ab|
$$

Ainsi
$$ (a \land b) \times (a \lor b) = |a \times b|
$$

#### Remarque

La formule suivante est **fausse**:
$$
(a \land b \land c) \times (a \lor b \lor c) = |a \times b \times c|
$$

## Nombres premiers

### Définition
#### Définition *Nombre premier*

Soit $p ∈ \mathbb{N}, p \ge 2$, $p$ est un nombre premier s'il n'admet pas d'autres diviseur positifs que 1 et lui-même.

Sinon on l'apelle nombre composé.

L'ensemble des nombres premiers se note $\mathbb{P}$ 

### Décomposition en produit de facteurs premiers

#### Théorème "Décomposition en produit de facteurs premiers"

$$
∀ n ∈ \mathbb{N}, n \ge 2, ∃ r ∈ \mathbb{N}^{*}, p_1, \cdots p_r ∈ \mathbb{P}, ∃ α _1, \cdots, α _r ∈ \mathbb{N}^{*} / n = \prod_{i=1}^{n} p_i^{α _i}
$$

De plus cette composition est **UNIQUE** (a l'ordre des facteurs près)

#### Preuve de l'existence

On procède par récurrence forte sous $n \ge 2$

La propriété est vraie pour $n = 2$ car c'est un nombre premier. 

On suppose donée $n \ge 2$ telque tous les entiers allant de 2 a $n$  soit décomposables en un produit de facteurs premiers. Montrons que c'est le cas pour l'entier $n+1$.

Si $n+1$ est un nombre premier alors $n+1$ est déjà décomposé

Sinon $n+1$ est composé donc
$$
∃ a, b ∈ \mathbb{N}, 2 \le a,b \le n / n+1 = ab
$$ 

Par hypothèse de récurrence donc $a$ est décomposé et $b$ l'est aussi, ainsi la décomposition de $n+1$ ce fait par le produit de celles de $a$ et de $b$  

#### Preuve de l'unicité

#### Lemme "Lemme clef"

Soit $r ∈ \mathbb{N}^{*}$ et $p,p_1, \cdots, p_r ∈ \mathbb{P}$

Si
$$
p | \prod_{i=1}^{r} p_i
$$ 

Alors $∃ 1 \le i \le r / p = p_i$

##### Preuve

Pour $r = 1$ on a $p | p_1$ donc $p ∈ \{1, p_1\}$ or $1 ∉ \mathbb{P}$ donc $p = p_1$

Supposons que la propriété soit vraie au rang $r$ montrons la au rang $r+1$

Si $p$ divise $p_{r+1}$ alors $p = p_{r+1}$ (voir initialisation)

Sinon $p$ ne divise pas $p_{r+1}$ alors $p \land p_{r+1} = 1$

> Soit $d$ un diviseur commun a $p$ et $p_{r+1}$ donc comme $p ∈ \mathbb{P}$ on a que $d ∈ \{1, p\}$.
>
> Or si $d = p$ alors $p | p_{r+1}$ mais par hypothèse ce n'est pas le cas donc $d = 1$

$$
p | \prod_{i=1}^{r+1} p_i = \prod_{i=1}^{r} p_i \times p_{r+1}
$$

Donc d'après Gauss, $p | \prod_{i = 1}^{r} p_i$

Enfinpar hypothèse de récurrence,
$$
∃ 1 \le i \le r / p = p_i
$$

##### Preuve de l'unicité

Avec les notations entendues, on suppose que
$$
\prod_{i=1}^{r} p_i^{α _i} = \prod_{j = 1}^{s} q_j^{β _j}
$$

Montrons que $r = s$

Soit $1 \le i \le r$

On sait que $p_i | \prod_{i=1}^{n} p_i^{ α _i} = \prod_{j=0}^{s} q_j ^{ β_j}$

DOnc d'après le lemme,
$$
p_i ∈ \{ q_j / 1 \le j \le s \}
$$

Donc
$$
\{ p_i / 1 \le i \le r \} ⊂ \{ q_j / 1 \le j \le s \}
$$

Par symmétrie des roles des 2 décompositions on a

$$
\{ q_j / 1 \le j \le s \} ⊂ \{ p_i / 1 \le i \le r \}
$$

Donc $\text{card}(q_j) = \text{card}(p_i) \iff r = s$ et quitte a permuter les elements, on a:

$$
∀ 1 \le i,j \le r,s, p_i = q_j
$$

Montrons que $∀ 1 \le i \le r, α _i = β _i$

Par l'absurde, $∃ 1 \le j \le r / α _j \neq β _j$

On ne restreint pas la généralité en supposant que
$$
α _j > β _j
$$

On a que 

$$
p_j^{ α _j} \times \prod_{i=1}^{r} p_i ^{α _i} = p_j ^{β _j} \times \prod_{i = 1}^{ r} p_i ^{ β _j}
$$

$$
p_j^{ α _j - β _j} \times \prod_{i=1}^{r} p_i ^{α _i} =  \prod_{i = 1}^{ r} p_i ^{ β _j}
$$

Or $p_j ^{α _j - β _j} \times \prod_{i = 1}^{r} p_i^{α _i}$ est divisible par $p_j$

Donc
$$
p_j | \prod_{i=1}^{r} p_i^{β _i}
$$

Donc d'après le lemme, $∃ p_i = p_j$
Ceci contredit le fait que $p_1, \cdots, p_r$ sont deux-a-deux distincts.

#### Corollaire
$\mathbb{P}$ est infini

#### Preuve

Par l'absurde on suppose que $\mathbb{P}$ est fini, alors on peut écrire
$$
\mathbb{P} = \{p_1, \cdots, p_r \}
$$

en extension.

On pose
$$
n = \prod_{i=1}^{r} p_i + 1
$$ 

On décompose $n$ en un produit de nombres premiers

Donc il existe $1 \le j \le r$ elque $p_j$ divise $n$

$$
p_j | \prod_{i=1}^{r} p_i
$$

Donc $p_j$ divise $n - \prod_{i=1}^{r} p_i = 1$

Ce qui est absurde.

#### Corollaire "Lemme d'Euclide"

Soient $a, b ∈ \mathbb{Z}$, soit $p ∈ \mathbb{P}$ 

Si $p | a \times b$ alors $p | a$   ou $p | b$ .

#### Preuve

Il suffit de prouver le résultat pour $a$ et $b$ dans $\mathbb{N}$

On décompose $a$ et $b$:
$$
a = \prod_{i=1}^{r} p_i^{α _i}, b = \prod_{j=1}^{s} p_j^{β _j}
$$  

Or $p | a \times b$ donc $∃ k ∈ \mathbb{N}^{*} / a \times b = kp$

On décompose également $k$ et on a:
$$
k = \prod_{l=1}^{t} r_l^{γ _l}
$$ 

Donc
$$
\prod_{i = 1}^{r} p_i^{α _i} \times \prod_{j = 1}^{ s} p_j ^{ β _j} = p \times \prod_{l=1}^{t} r_l^{γ _l}
$$

Par unicité de l'écriture, $p ∈ p_i$ ou $p ∈ p_j$  

### Valuation p-adique

Soit $n ∈ \mathbb{Z} \backslash \{0\}$

On note
$$
A = \{ k ∈ \mathbb{N} / p^{k} | n\}
$$

$A ⊂ \mathbb{N}$ donc d'après l'axiome de Péano on souhaite montrer qu'il admet un maximum.

$A \neq \varnothing$, et il est majoré par $\lfloor \log_p(|n|)\rfloor + 1$   

Il admet donc un maximum noté $v_p(n)$

#### Définition *Valuation $p$-adique de $n$*

On appelle valuation $p$-adique de $n$ le nombre défini par:
$$
\text{max}\left( \{  k ∈ \mathbb{N} / p^{k} | n \} \right), \text{ si } n \neq 0
$$
$$
+\infty \text{ sinon} 
$$

#### Remarque

Si $k ∈ A$ et $k ∈ \mathbb{N}^{*}$ alors $k-1 ∈ A$, ainsi on a
$$
A = \{0,1,2,\cdots, v_p(n)\}
$$

#### Théorème

Soit $n \ge 2$

Alors
$$
n = \prod_{p ∈ \mathbb{P}} p^{v_p(n)}
$$

Ce produit est bien un produit **fini** car a partir d'un certain rang, tous les autres termes sont unitaires. (Un nombre possède un nombre fini de diviseurs premiers)

#### Preuve

On décompose $n$ en un produit de  nombre premiers
$$
n = \prod_{i=1}^{r} p_i^{ α _i}
$$

Soit $p ∈ \mathbb{P}$ 

**Cas n⁰1**: Si $p ∉ \{p_1, \cdots, p_r\}$

Si $p | n$ alors $∃ 1 \le j \le r / p = p_i$

Absurde.

Donc $p$ ne divise pas $n$ donc $v_p(n) = 0$

**Cas n⁰2**; Si il existe $1 \le j\le r / p=p_i$

D'ou, $p^{α _j} | n \iff v_p(n) \ge α _j$

Si $p^{ α _j +1 } | n$ alors $p | \prod_{i = 1, i \neq j}^{r} p_i^{ α _i}$

Ainsi $∃ 1 \le i \neq j \le r / p = p_i$

Ce qui est absurde.

Donc $p^{α _j  + 1}$ ne divise pas $n$ donc $v_p(n) < α _j + 1$

Donc $v_p(n) = α _j$ 

Donc
$$
\prod_{p ∈ \mathbb{P}} p ^{v_{p}(n)}  = \left(\prod_{i=1}^{r} p_i ^{v_{pi}(n)} \right) \times \left( \prod_{p ∈ \mathbb{P} \backslash \{p_1, \cdots p_r\}}\right) = n
$$

#### Remarque

Cette formule marche aussi pour 1

#### Théorème

Soient $a,b ∈ \mathbb{Z}$

$∀ p ∈ \mathbb{P}, v_p(a \times b) = v_p (a) + v_p (b)$ 

#### Preuve

- Quitte a remplacer $a$ par $-a$ ou $b$ par $-b$ on peut supposer que $a,b ∈ \mathbb{N}$     

- La formule est vraie si $a \text{ ou } b = 0$ donc on peut supposer $a,b ∈ \mathbb{N}^{*}$ 

- $a = \prod_{p ∈ \mathbb{P}} p^{v_p(a)}$, $b = \prod_{p ∈ \mathbb{P}} p^{v_p(b)}$ 


- $a \times b = \prod_{p ∈ \mathbb{P}} p^{v_p(a) + v_p(b)}$ 

or

- $a \times b= \prod_{p ∈ \mathbb{P}} p^{v_p(a \times b)}$ 

Donc

$v_p(a \times b) = v_p(a + b)$ 

#### Théorème

Soient $a, b ∈ \mathbb{Z}$

$a | b$

si, et seulement si,

$∀ p ∈ \mathbb{P}, v_p(a) \le v_p(b)$ 

#### Preuve
On ne restreitn pas la généralité en prouvant le théoreme pour $a,b ∈ \mathbb{N}^{*}$

#### Preuve
" $\implies$" :

Soit $p ∈ \mathbb{P}, p^{v_p(a)} | a,b$ 

ainsi $v_p(a) ∈ \{ k ∈ \mathbb{N} / p^{k} | b\}$, donc $v_p(a) \le v_p(b)$ 

" $\impliedby$ " :
$$
b = \prod_{p ∈ \mathbb{P}} p^{v_p(b)} = \prod_{p ∈ \mathbb{P}} p^{v_p(a)} \times \prod_{p ∈ \mathbb{P}} p^{v_p(b) - v_p(a)}
$$ 

Donc $a  | b$ 

#### Exercice

Proposer une troisiemme preuve du lemme d'euclide

$p | a \times b \iff v_p(p) \le v_p( a\times b)$ donc $1 \le v_p(a) + v_p(b)$

Donc $v_p(a) \ge 1$ ou $v_p(b) \ge 1$  

Donc $p | a$ ou $p | b$  

#### Théorème

Soient $a,b ∈ \mathbb{Z} \backslash \{0\}$

$$
a \land b = \prod_{p ∈ \mathbb{P}} p^{\text{min}(v_p(a), v_p(b))}
$$

$$
a \lor b = \prod_{p ∈ \mathbb{P}} p^{\text{max}(v_p(a), v_p(b))}
$$

#### Conséquences

$v_p(a \land b) = \text{min}(v_p(a), v_p(b))$

$v_p(a \lor b) = \text{max}(v_p(a), v_p(b))$ 

#### Preuve

- Soit $p ∈ \mathbb{P}$ 
- $a \land b  | a \implies v_p(a \land b) \le v_p(a)$ 
- $a \land b  | b \implies v_p(a \land b) \le v_p(b)$
- $a \land b  | a,b \implies v_p(a \land b) \le \text{min}(v_p(a),v_p(b))$

donc
$$
\prod_{p ∈ \mathbb{P}} p^{v_p(a \land b)} | \prod_{p ∈ \mathbb{P}} p^{\text{min}(v_p(a), v_p(b))}
$$ 

Car si $a | c$ et si $b | d$ alors $ab  | cd$    

Donc

$$
a \land b | \prod_{p ∈ \mathbb{P}} p^{\text{min}(v_p(a), v_p(b))}
$$

Donc $\text{min}(v_p(a), v_p(b) \le v_p(a) \iff p^{\text{min}\cdots} | p^{v_p(a)}$ 

Donc
$$
\prod_{p ∈ \mathbb{P}} p^{\text{min} \cdots} | \prod_{p ∈ \mathbb{P}} p^{v_p(a)} = a
$$


$$
\prod_{p ∈ \mathbb{P}} p^{\text{min} \cdots} | \prod_{p ∈ \mathbb{P}} p^{v_p(b)} = b
$$

Donc
$$
\prod_{p ∈ \mathbb{P}} p^{\text{min} \cdots} | a, b \iff \prod_{p ∈ \mathbb{P}} p^{\text{min} \cdots} | a \land b
$$

#### Théorème

Soient $a, b ∈ \mathbb{Z}, p ∈ \mathbb{P}$

- $v_p(a+b) \ge \text{min}(v_p(a), v_p(b))$ 
- En général il n'y a pas d'égalité

Si $v_p(a) \neq v_p(b)$ alors $v_p(a+b) = \text{min}(v_p(a), v_p(b))$ La reciproque est fausse.

#### Preuve
Comme avant, $a, b ∈ \mathbb{N}^{*}$

On suppose que $v_p(a) \le v_p(b)$ quitte a echanger les roles 

$$
p^{v_p(a)} | a, p^{v_p(b)} | b \iff p^{v_p(a)} | b
$$

Donc $p^{v_p(a) | a + b}$ 

Pour $p = 2, a = 2, b = 14$ alors $v_2(16) = 4 \neq 1 = v_2(2) = v_2(14)$

On suppose $v_p(a) < v_p(b)$

$p^{v_p(a)} | a$, $p^{v_p(a)+1} | b$

Donc $p^{v_p(a)} | a+ b (*)$

mais $p^{v_p(a) + 1}$ ne divise pas $a+b (**)$  

- $(*)$ est vraie car $p^{v_p(a)} | b$ donc par combinaison lineaire.
- $(**)$, supposons que $p^{v_p(a)+1} | a + b$ alors $p^{v_p(a) + 1} | a+ b - b = a$

Donc $v_p(a) + 1 \le v_p(a) \iff 1 < 0$, absurde. 

## Congruences

### Définition et exemples

#### Définition

$$
a \equiv b [n] \iff a = nq + r, b = nq' +r , q, q' ∈ \mathbb{Z}
$$

#### Théorèmem
