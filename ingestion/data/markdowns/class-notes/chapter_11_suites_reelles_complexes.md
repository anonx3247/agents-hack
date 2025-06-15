# Chapitre 11: Suites a valeurs reelles ou complexes

Dans ce chapitre on etudie les suites (en commencant par les reelles, puis on feras les complexes).

## Generalites sur les suites

#### Définition *suite*

Une suite $u$ notee $(u_n)$ est une application de $\mathbb{N}$ dans $\mathbb{R}$.

#### Définition *suite croissante/decroissante/monotone*

On dit que $u$ est croissante si:
$$
∀ n ∈ \mathbb{N}, u_{n+1} \ge u_n
$$
On dit que $u$ est decroissante si:
$$
∀ n ∈ \mathbb{N}, u_{n+1} \le u_n
$$
On dit qu'une suite est monotone si elle est croissante ou decroissante.

#### Définition *suite majoree/minoree/bornee*

On dit que $u$ est majoree si:
$$
∃ M ∈ \mathbb{R} / ∀ n ∈ \mathbb{N}, u_n \le M
$$
On dit que $u$ est minoree si:
$$
∃ m ∈ \mathbb{R} / ∀ n ∈ \mathbb{N}, u_n \ge m
$$
 On dit que $u$ est bornee si elle est minoree et majoree.

#### Théorème

Une suite $(u_n)$ est bornee si et seulement si:
$$
∃ M ∈ \mathbb{R} / ∀ n ∈ \mathbb{N}, |u_n| \le M
$$

  #### Preuve

- " $\implies$ " si $m \le u_n \le M$ alors $|u_n| \le \max(M, -m)$
- " $\impliedby$ " si $|u_n| \le M$ alors $-M \le u_n \le M$    

## Convergence et divergence des suites

### Generalites

#### Définition *suite convergente*

$u$ est **convergente** si:
$$
∃ l ∈ \mathbb{R}/ ∀ ε > 0, ∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, n \ge N \implies |u_n - l| \le ε )
$$


#### Théorème

Si $(u_n)$ converge alors sa le $l$ de la definition precedente est unique, elle s'appelle la **limite** de la suite $(u_n)$ et on note:
$$
l = \lim_{n\to\infty} u_n
$$
$l$ est unique.

#### Preuve

Soit $l,l'$ deux limites de $(u_n)$.

Raisonnons par l'absurde, on suppose que $l \neq l'$.

Choisissons $ε = |l - l'|$. 

Comme $(u_n)$ converge vers $l$ on a:
$$
∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, n \ge N \implies |u_n-l| \le |l-l'|
$$
 Comme $(u_n)$ converge vers $l'$ on a:
$$
∃ N' ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, n \ge N' \implies |u_n-l'|\le |l-l'|
$$
Posons $N'' = \max(N, N')$ de sorte que:
$$
∀ n ∈ \mathbb{N}, n \ge N'' \implies (|u_n-l| \le |l-l'| \land |u_n-l'| \le |l-l'|)
$$
 donc:
$$
|l-l'| = |l-u_{N''} + u_{N''} - l'| \le |l-u_{N''}| + |u_{N''}-l'| \le |l-l'| + |l-l'|
$$
d'apres les inegalites triangulaires.

donc
$$
|l'-l| \le 2|l-l'| \\
1 \le 2 \text{ }(*)
$$
On a pas d'absurdite.

avec $ε = \frac{|l-l'|}{2}$ on obtient:
$$
1 \le 1 \text{ } (*)
$$
avec $ε  = \frac{|l-l'|}{3}$, on obtient:
$$
1 \le \frac{2}{3} \text{ } (*)
$$
 Ce qui est absurde.

#### Définition *suite divergente de premierre espece*

On dit que $(u_n)$ tend vers $+\infty$, et on note
$$
\lim_{n\to+\infty} u_n = +\infty
$$
  si:
$$
∀ A ∈ \mathbb{R}, ∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, (n  \ge N \implies u_n \ge A)
$$
On dit que $(u_n)$ tend vers $-\infty$, et on note:
$$
\lim_{n\to+\infty} u_n = -\infty
$$
  si:
$$
∀ A ∈ \mathbb{R}, ∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, (n \ge N \implies u_n \le A)
$$
Dans ces deux cas on dit que $(u_n)$ est divergente de *premierre espece*.

#### Définition *suite divergente de deuxieme espece*

Si $(u_n)$ n'est ni convergente, ni divergente de premierre espece alors on dit que $(u_n)$ n'admet pas de limite et on dit que $(u_n)$ est divergente *de second espece*.

#### Exemples

- Montrons que $u_n = \frac{1}{n}$ converge vers $0$.

  Soit $ε > 0$, 

  Posons $N = \lfloor \frac{1}{ε } \rfloor + 1$, donc $N  \ge ε $

  Soit $n ∈ \mathbb{N} / n \ge N$.

$$
|u_n - 0| \le \frac{1}{n} \le \frac{1}{N} \le ε
$$

- Montrons que $v_n = n$ diverge vers $+\infty$

  Posons   $N = \lfloor A \rfloor + 1$

  donc $u_n  = n  \ge N \ge A$  

- Montrons que $w_n = (-1)^{n}$ n'admet pas de limite.

  $-1 \le w_n \le 1$ donc $w_n$ n'est pas diveregente de premierre espece.

  montrons que $(w_n)$  n'est pas convergente en raisonnant par l'absurde, on suppose qu'elle converge vers $l$.

  Choisissons $ε = 1$.
  $$
  ∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, (n \ge N \implies |u_n - l| \le 1)
  $$

  $$
  |u_{N+1} - u_{N}| = 2 \implies |u_{N+1} - l + l u_{N}| = 2 \\
  2 \le |u_{N+1} - l| + |l - u_N| \\
  2 \le 1 + 1 \\
  \text{ on pose } ε = \frac{1}{2} \\
  2 \le \frac{1}{2} + \frac{1}{2}
  $$

  

#### Théorème de Cesaro

- Soit $(u_n)$ une suite qui converge vers $l$.
- Pour $n ∈ \mathbb{N}$, on pose $v_n = \frac{∑_{k=0}^{n} u_k}{n+1}$    
- Monstrons que $v_n$ converge vers $l$.
- (A faire) 

#### Théorème

Une suite convergente est bornee.

(La reciproque est **fausse**).

#### Preuve

$u_n \to l$. On choisi $ε = 1$ dans la definition de la convergence:
$$
∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, n \ge N \implies|u_n - l| \le 1
$$
Ainsi, 
$$
∀ n ∈ \mathbb{N}, |u_n| = |u_n - l + l| \le |u_n - l| + |l| \le  1 + |l| \\
∀ n ∈ \mathbb{N}, |u_n| \le 1 + |l|
$$
Donc $∀ n ∈ \mathbb{N}, |u_n| \le \max(|u_0|, |u_1|, \cdots |u_{N-1}|, 1 + |l|)$ 

Donc $u_n$ est bornee.

#### Théorème

On suppose que $(u_n)$  converge vers $l$,
$$
l > 0 \implies ∃ N ∈ \mathbb{N} /  ∀ n ∈ \mathbb{N}, u_n > 0
$$

   #### Remarque

Ce theoreme est faux avec des ineglaites larges ( $\le$ ), 

en effet $(-\frac{1}{n})$ converge vers $0$, on a $0 \le 0$ mais $-\frac{1}{n}$ est negative.    

#### Preuve

On choisi $ε = l$ dans la definition de la convergence.
$$
∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, n\ge N \implies|u_n - l| \le l
$$
Soit $n ∈ \mathbb{N} / n \ge N$.

 $u_n = u_n - l + l \ge -|u_n-l| + l \ge -l + l = 0$  

Donc on choisi $ε = \frac{l}{2}$. 

#### Corollaire

On suppose que $u_n \to l$, si
$$
α < l < β \implies ∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, α < u_n < β
$$

### Operations sur les limites

#### Somme

#### Théorème

Soit $(u_n)$ et $(v_n)$ 2 suites qui admettent une limite.

On a:

| $\lim u_n$       | $l_1$     | $l_1$     | $l_1$     | $+\infty$ | $-\infty$ | $+\infty$ |
| ---------------- | --------- | --------- | --------- | --------- | --------- | --------- |
| $\lim v_n$       | $l_2$     | $+\infty$ | $-\infty$ | $+\infty$ | $-\infty$ | $-\infty$ |
| $\lim u_n + v_n$ | $l_1+l_2$ | $+\infty$ | $-\infty$ | $+\infty$ | $-\infty$ | $?$       |

#### Preuve

Montrons que si $(u_n)$ converge vers $l_1$ et $(v_n)$ vers $l_2$, alors $u_n+v_n$ converge vers $l_1+l_2$

Soit $ε > 0$.

Comme $(u_n)$ converge vers $l_1$ alors $∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, (n \ge N \implies |u_n - l_1| \le ε )$

Comme $(v_n)$ converge vers $l_2$ alors $∃ N' ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, (n \ge N' \implies |v_n - l_2| \le ε )$

On pose $N'' = \max(N, N')$, Soit $n ∈ \mathbb{N} / n \ge N''$ .
$$
|u_n + v_n - (l_1+l_2) | \le |u_n - l_1| + |v_n - l_2|
$$
Par inegalite triangulaire.

Donc:
$$
|u_n + v_n - (l_1+l_2) | \le 2 ε 
$$

#### Multiplication par un scalaire

#### Théorème

Soit $(u_n)$ une suite qui admet une limite, et considerons $λ ∈ \mathbb{R}^{*}$.

| $\lim u_n$   | $l_1$   | $+\infty$  | $-\infty$    |
| ------------ | ------- | ---------- | ------------ |
| $\lim λ u_n$ | $λ u_n$ | $λ \infty$ | $- λ \infty$ |

#### Produit

#### Théorème

Soit $(u_n)$ et $(v_n)$ 2 suites qui admettent une limite.

On a:

| $\lim u_n$     | $l_1$    | $l_1 \neq 0$ | $l_1 \neq 0$  | $0$         | $\pm\infty$  |
| -------------- | -------- | ------------ | ------------- | ----------- | ------------ |
| $\lim v_n$     | $l_2$    | $+\infty$    | $-\infty$     | $\pm\infty$ | $\pm\infty$  |
| $\lim u_n v_n$ | $l_1l_2$ | $l_1 \infty$ | $-l_1 \infty$ | $?$         | $\pm \infty$ |

#### Preuve

Montrons que si $(u_n)$ converge vers $l_1$ et $(v_n)$ vers $l_2$, alors $u_n+v_n$ converge vers $l_1+l_2$

Soit $ε > 0$.

Comme $(u_n)$ converge vers $l_1$ alors $∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, (n \ge N \implies |u_n - l_1| \le ε )$

Comme $(v_n)$ converge vers $l_2$ alors $∃ N' ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, (n \ge N' \implies |v_n - l_2| \le ε )$

On pose $N'' = \max(N, N')$, Soit $n ∈ \mathbb{N} / n \ge N''$ .
$$
|u_n \times v_n - (l_1\times l_2) |  \iff |(u_n - l_1 + l_1) \times v_n - l_1l_2| \\
\iff |(u_n-l_1) \times v_n + l_1(v_n-l_2)| \\
\le |u_n - l_1 | \times |v_n| + |v_n-l_2| \times |l_1| \\
\le ε \times (|v_n| + |l_1|) \\
\le ε \times (C + |l_1|)
$$
avec $C$ le maximum de $|v_n|$ (elle a un maximum car elle est convergente, donc bornee.)

#### Passage a l'inverse

#### Théorème

Soit $(u_n)$ une suite admettant une limite et a valeurs dans $\mathbb{R}^{*}$ a partir d'un certain rang   

| $\lim u_n$           | $l_1 \neq 0$    | $+\infty$ | $-\infty$ | $0^{+}$   | $0^{-}$   |
| -------------------- | --------------- | --------- | --------- | --------- | --------- |
| $\lim \frac{1}{u_n}$ | $\frac{1}{l_1}$ | $0$       | $0$       | $+\infty$ | $-\infty$ |

#### Preuve

Exercice: montrer que si $(u_n)$ converge vers $l_1 \neq 0$ alors $\frac{1}{u_n}$ converge vers $\frac{1}{l_1}$.

Initialisation: montrer que $|u_n| \ge \frac{|l_1|}{2}$ a partir d'un certain rang.      

### Les theoremes de comparaison

#### Cas de convergence

#### Théorème "Theoreme de comparaison des limites"

Soient $(u_n), (v_n)$, 2 suites telles que $u_n \ge v_n$ a partir d'un certain rang.

On suppose que $(u_n), (v_n)$ convergent en $l_1, l_2$ respectivement.

Alors on a $l_1 \le l_2$ .

#### Remarque

$\neg (u_n < v_n \implies \lim u_n < \lim v_n)$     

plutot:

$(u_n < v_n \implies \lim u_n \le \lim v_n)$ 

#### Preuve

Soit $ε > 0$.

Soient $N_1 ∈ \mathbb{N} / ∀ n  \ge N_1, un \le v_n$.

Comme $u_n$ converge vers $l_1$ alors:
$$
∃ N_2 ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, |u_n - l_1| \le ε 
$$
Comme $v_n$ converge vers $l_1$ alors:
$$
∃ N_3 ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, |v_n - l_2| \le ε 
$$
  Soit $N = \max(N_1, N_2, N_3)$
$$
l_1 = l_1 - u_N + u_N \\
\le |l_1 - u_N| + u_N \\
\le ε + v_N \\
\le ε + v_N + l_2 - l_2 \\
\le ε + |v_N - l_2 | + l_2 \\
\le 2ε + l_2
$$
 Donc $∀ ε > 0, l_1 < l_2 + 2 ε $.

Raisonnons par l'absurde, 

Supposons que $l_1 > l_2$.

On choisi $ε = \frac{l_1 - l_2}{4}$:
$$
l_1 < l_2 + 2\left(\frac{l_1 - l_2}{4}\right) \\
\frac{l_1}{2} < \frac{l_2}{2} \\
l_1 \le l_2
$$
C'est bien absurde.

#### Théorème "Theoreme d'Encadrement"

Soit $u_n, v_n, w_n$ verifiant, a partir d'un certain rang:
$$
u_n \le v_n \le w_n
$$
Si $u_n, w_n$ convergent vers la meme limite $l$, alors

$v_n \to l$.

#### Preuve

Soit $N_1 ∈ \mathbb{N} / ∀ n \ge N_1, u_n \le v_n \le w_n$.

Soit $ε > 0$.

Comme $u_n \to l$ alors:
$$
∃ N_2 ∈ \mathbb{N} / ∀ n > N_2, |u_n - l| \le ε 
$$
Comme $w_n \to l$ alors:
$$
∃ N_3 ∈ \mathbb{N} / ∀ n \ge N_3, |w_n - l| \le ε
$$
On pose $N = \max(N_1, N_2, N_3)$.

Comme $u_n \le v_n \le w_n$:
$$
u_n - l \le v_n - l \le w_n - l
$$
   d'ou:
$$
|v_n - l| \le \max(|u_n - l|, |w_n - l|) \le ε 
$$
Donc $v_n \to l$ .

#### Exercice

Si $(u_n)$ est bornee et $(v_n) \to 0$ alors $(u_n \times v_n)$ converge vers $0$.

On pose $m \le u_n \le M$.

$v_n \times m \le u_n \times v_n \le v_n \times M$ 

Si $v_n < 0$ alors on echange $m$ et $M$.   

Or $v_n \times m \to 0$ et $v_n \times M \to 0$ donc par encadrement:

$v_n \times u_n \to 0$.

#### Conseil

Pour trouver que $(a_n) \to 0$ on peut essayer de majorer la valeur absolue par une suite tendant vers 0.

#### Théorème "Theoreme de la limite monotone"

Toute suite $\nearrow$ et majoree, converge, et toute suite $\searrow$ et minorree converge.     

#### Preuve

... (A revoir)

#### Remarque

Si $u_n$ est une suite $\nearrow$ alors:

- Si $u_n < M$ alors $u_n \to l$
- Sinon, $u_n \to +\infty$   

#### Théorème "Theoreme des suites adjacentes"

Soient $u_n,v_n$, on suppose que:

-  $u_n \nearrow \land v_n \searrow$
- $u_n - v_n \to 0$
- alors $(u_n),(v_n) \to l$

Elles convergent vers **la meme limite**.

#### Preuve

Soit $n ∈ \mathbb{N}$

Pour $∀ p ∈ \mathbb{N}, u_{n+p} \nearrow, v_{n+p} \searrow$.

donc $u_{n+p} - v_{n+p} \nearrow$.

Donc $∀p ∈ \mathbb{N}, u_{n+p} - v_{n+p} \ge u_n - v_n$ 

En faisant tendre $p\to+\infty$, on obtient:
$$
0 \ge u_n - v_n \iff v_n \ge u_n
$$
 Donc $∀ n ∈ \mathbb{N}, u_0 \le u_n \le v_n \le v_0$ 

Ainsi $u_n \nearrow, u_n \le M$ donc $u_n \to l_1$ selon theoreme de limite monotone.

Ainsi $v_n \searrow, v_n \ge m$ donc $v_n \to l_2$ selon theoreme de limite monotone.

Or:
$$
u_n - v_n \to 0 \land u_n - v_n \to l_1 - l_2 \iff l_1 = l_2
$$
Donc elles ont bien la meme limite.

#### Cas de divergence

#### Théorème

On suppose, donne $u_n, v_n / ∃ N ∈ \mathbb{N} / ∀ n \ge N, u_n  \le v_n$

Si $u_n \to +\infty$ alors $v_n \to +\infty$ et 

Si $v_n \to -\infty$ alors $u_n \to -\infty$.

## Le theoreme de Bolzano-Weierstrass

### Suite extraite

#### Définition *Suite Extraite*

On appelle suite extraite de $(u_n)$ (ou sous-suite) toute suite de la forme $u_{φ (n)}$ ou $φ $ est une application de $\mathbb{N}$ dans $\mathbb{N}$ **strictement croissante**.

#### Exemples

- $(u_{2n})$ et $(u_{2n+1})$ sont des sous suites
- $(u_{\frac{n}{2}})$  n'est pas une sous suite.

#### Théorème
Si $(u_n)\to l \in \overline{\mathbb{R}}$ alors toutes les sous suites de $(u_n)$ tendent vers $l$.

#### Lemme
Si $φ $ est strictement croissante de $\mathbb{N}$ dans $\mathbb{N}$ alors $∀ n ∈ \mathbb{N}, φ (n) \ge n$

#### Preuve

Prouvons le par recurrence:

$φ (0) \ge 0$ car $φ $ est a valeurs dans $\mathbb{N}$.
On suppose que $φ (n+1) > φ (n) \ge n$.

D'ou
$$
φ (n+1) > n \iff φ (n) \ge n
$$

#### Preuve du theoreme

Cas ou $l∈\mathbb{R}$:

On suppose que $(u_n)\to l$.

Soit $φ : \mathbb{N} \to \mathbb{N}$ strictement $\nearrow$.

Montrons que $(u_{φ (n)})\to l$.
$$
∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, (n\ge N \implies |u_n - l| \le ε )
$$

Soit $n ∈ \mathbb{N} / n \ge N$ on a donc $φ (n) \ge N \implies |u_{φ (n)} - l| \le ε $.

#### Remarque

Ce resultat est tres utile sous sa forme contraposee. Pour montrer qu'une suite est divergente de 2nd espece (qu'elle n'admet pas de limite) il suffit d'exhiber de sous suite qui convergent vers des limites differentes

#### Exemple $u_n = (-1)^{n}$
$$
u_{2n} \to 1 \land u_{2n+1} \to -1 \iff u_n \to \varnothing
$$ 


#### Théorème

Si $u_{2n}$ et $u_{2n+1}$ convergent vers la meme limite alors $(u_n)$ converge.

#### Remarque

Ceci fonctionne pour toute collection de sous-suites dont l'union est egal a $(u_n)$ en particulier des partitions de $(u_n)$  

#### Preuve

Soit $ε > 0$ Notons $l = \lim_{n\to+\infty} u_{2n}=\lim_{n\to+\infty} u_{2n+1}$

Comme $(u_{2n})$ converge vers $l$ on a :
$$
∃ N_1 ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, (n \ge N_1 \implies |u_{2n}-l| \le ε )
$$  

Comme $(u_{2n+1})$ converge vers $l$ on a :
$$
∃ N_2 ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, (n \ge N_2 \implies |u_{2n+1}-l| \le ε )
$$  

On pose alores $N = \text{max}(N_1, N_2)$ et $M = 2N+1$ 

Soit $n ∈ \mathbb{N} / n \ge M$

Si n est pair alors il existe $ p ∈ \mathbb{N} / n = 2p$ 

Or $n \ge M = 2N+1 \ge 2N \ge 2N_1 \iff p \ge N_1$

donc $|u_{2p} - l| \le ε \iff |u_n - l| \le ε $

Si n est impair alors il existe $ p ∈ \mathbb{N} / n = 2p+1$ 

Or $n \ge M = 2N+1 \ge 2N_2 +1 \iff p \ge N_2$

donc $|u_{2p+1} - l| \le ε \iff |u_n - l| \le ε $

A faire: demontrer pour $u_{kn} \cdots u_{kn+(k-1)}$ 

### Le theoreme de Bolzano-Weiestrass

#### Rappel

Si $(u_n)\to l ∈ \overline{\mathbb{R}}$ alors $(u_n)$ est bornee.

La reciproque est fausse, mais vraie pour une sous-suite.

#### Théorème de Bolzano-Weiestrass

De toute suite bornee, on peut extraire une sous-suite convergente.

#### Preuve

Soit $(u_n)$ une suite bornee.

> On imagine qu'on est sur une ile constituee d'hotels, avec le nombre de l'hotel (n) et leurs hauteurs $(u_n)$
> On introduit l'ensemble A des hotels ayant vue sur la mer (i.e d'hauteur superieur ou egale au hotels qui les suivent.)

$$
A = \{ n ∈ \mathbb{N} / ∀ p > n, u_n > u_p \}
$$

Cas 1: avec $\text{card}(A) = +\infty$.

> Comme A est infini on sait qu'a partir d'un certain rang il y auras une infinite d'hotels voyant la mer tous plus petit que ceux d'avant (ainsi on peut extraire la soussuite qui a tous les membres de A qui est strictement decroissante)

On construit par recurrence forte une sous-suite $(φ (n))$ strictement croissante de $\mathbb{N}$ dans $\mathbb{N}$ a valeurs dans $A$:
- On pose $φ (0) = \text{min}(A)$
- On suppose donne $n ∈ \mathbb{N} / φ (0) \cdots φ (n)$ soient construits
construisons $φ (n+1)$

On pose $φ (n+1) = \text{min} A \backslash \{ 0, 1, \cdots, φ (n) \}$

D'ou $φ (n+1) ∈ A \land φ (n+1) > φ (n)$  

Recurrence achevee.

Soit $n ∈ \mathbb{N}$ comme $φ (n) ∈ A$ alors $∀ forallp  > φ (n), u_{φ (n)} > u_p$   

On choisi $p = φ (n+1)$ donc $u_{φ (n)} > u_{φ (n+1)}$ donc $u_{φ (n)}$ est strictement decroissante et minoree (car $(u_n)$ est bornee ) donc $u_{φ (n)}$ converge.

Cas 2: $A$ est fini.

Dans ce cas:
$$
∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, n \ge N, n ∉ A
$$

> Comme A est fini, on sait qu'a partir d'un certain hotel, on ne peut plus voir la mer, donc il existe une infinite d'hotels de plus en plus grands qui se cachent la mer les uns les autres.

On contruit par recurrence forte une suite $ψ (n)$ strictement croissante telle que:
$$
∀ n ∈ \mathbb{N}, u_{ψ (n)} \le u_{ψ (n+1)}
$$ 

On pose $ψ (0) = N$

On suppose donne $n ∈ \mathbb{N} / ψ (0), \cdots ψ (n)$ soient construits

or $ψ (n) \ge ψ (0) = N \iff ψ (n) ∉ A$

Ainsi $∃ p > ψ (n) / u_p \ge u_{ψ (n)}$ 

On pose $p = ψ (n+1)$:

On a donc $ψ (n+1) > ψ (n)$ et $u_{ψ (n+1)} > u_{ψ (n)}$

Recurrence achevee.

Donc $(ψ (n))$ est croissante et majoree donc elle converge. 

## Utilisation des usites pour etudier des proprietes topologiques de $\mathbb{R}$

### Lien avec la densite

#### Définition *A dense dans* $\mathbb{R}$

$A$ est dense dans $\mathbb{R}$ si pour tout intervalle $I$ de $\mathbb{R}$   ouvert et non vide, on a $A \cap I \neq \varnothing$

#### Exemple $\mathbb{R}$ est dense dans $\mathbb{R}$

#### Théorème "Caracterisation sequentielle de la densite"

Soit $A$ partie de $\mathbb{R}$, A est dense dans $\mathbb{R}$ si et seulement si tout reel est limite d'une suite d'elements de $A$.

C'est a dire:
$$
∀ x ∈ \mathbb{R}, ∃ (a_n) ∈ \mathbb{R}^{\mathbb{N}} / ∀ n ∈ \mathbb{N}, a_n ∈ A, \lim_{n\to+\infty} a_n = x
$$

#### Preuve

- "$\implies$ " Soit $x ∈ \mathbb{R}$, Pour $n ∈ \mathbb{N}$ on choisit $I = ] x - \frac{1}{n+1}, x + \frac{1}{n+1}[$ 

I est un intervalle ouvert et non vide donc comme A est dense dans $\mathbb{R}$, on a $A \cap I \neq \varnothing$, ainsi $∃ a_n ∈ A \cap I$   

On a donc une suite $(a_n)$ verifiant:
- $a_n ∈ A$
- $x - \frac{1}{n+1} < a_n < x + \frac{1}{n+1}$ 

Donc par encadrement $(a_n) \to x$

- "$\impliedby$ " Soit $I$ un intervalle ouvert et non vide de $\mathbb{R}$, montrons que $A \cap I \neq \varnothing$.

$I \neq \varnothing$ donc $∃ x ∈ I$  or $I$ est ouvert donc $I = I^{o}$ donc $∃ ε > 0 / [x- ε , x + ε ] ⊂ I$

Or par hypothese, il existe $(a_n) ∈ A ^{\mathbb{N}} / (a_n) \to x$

Ainsi $∃ N ∈ \mathbb{N} / ∀ n ∈ \mathbb{N}, n \ge N \implies |a_n - x| \le ε $
Donc $|a_n - x| \le ε $ donc $- ε < a_n - x < ε $ donc $x - ε < a_n < x + ε $. Puis $a_n ∈ [x- ε , x + ε ]$  donc $a_N ∈ I$, or $a_N ∈ A$ donc $A \cap I \neq \varnothing$.

$\mathbb{Q}$ est dense dans $\mathbb{R}$:
$$
x ∈ \mathbb{R}, \lim_{n\to+\infty} \frac{\lfloor nx \rfloor}{n}
$$

$\mathbb{R} \backslash \mathbb{Q}$ dense dans $\mathbb{R}$
$$
x ∈ \mathbb{R}, \lim_{n\to+\infty} \frac{\lfloor nx \rfloor}{n} + \frac{π }{n}
$$

#### Remarque

Tout intervalle ouvert non vide contient au moins un rationnel, un decimal et un irrationenel.

### Lien avec la borne superieur / inferieur:

#### Théorème

Soit $A ⊂ \mathbb{R}, A \neq \varnothing$ et majoree. Il existe une suite a valeurs dans $A$ qui converge vers $\text{sup}(A)$.

#### Preuve

Par la caracterisation de la borne superieur on a:
$$
∀ a ∈ A, a \le \text{sup}(A)
$$
et
$$
∀ ε > 0, ∃ a ∈ A / \text{sup}(A) - ε \le a
$$

Pour $n ∈ \mathbb{N}$, on choisi $ε = \frac{1}{n+1}$.

Il existe $a_n ∈ A / \text{sup}(A) - \frac{1}{n+1} \le a_n \le \text{sup}(A)$

Par encadrement $(a_n) \to \text{sup}(A)$.

#### Remarque
Ceci marche aussi pour la borne inferieur:

#### Théorème
Soit $A$ une partie de $\mathbb{R}$ non vide, minoree, il existe une suite a valeurs dans $A$ qui converge vers $\text{inf}(A)$.

## Croissances comparees

#### Théorème
- $∀ α , β ∈ \mathbb{R}^{+}, \lim _{n \to +\infty} \frac{\ln(n)^{α }}{n^{β   }} = 0$
- $∀ α ∈ \mathbb{R}^{+}, ∀ q > 1, \lim_{n\to +\infty} \frac{n^{α }}{q^{n}} = 0$ 
- $∀ q > 1, \lim_{n\to+\infty} \frac{q^{n}}{n!} =0$ 
- $\lim _{n \to +\infty} \frac{n!}{n^{n}} = 0$. 

#### Preuve

Pour $x \ge 1$ on pose $φ (x) = 2 \sqrt{x} - \ln x$

$φ $ est derivable sur $[1+\infty[$ et $∀ x \ge 1,$
$φ '(x) = \frac{1}{\sqrt{x}} - \frac{q}{x} = \frac{\sqrt{x} - 1}{x} \ge 0$
Donc $φ \nearrow$. SOnc $∀ x \ge 1, φ (x) φ (1) = 2 \ge 0$
- Donc $∀ x \ge 1, 2 \sqrt{x} \ge \ln x$.
- Donc $∀ x \ge 1, 0 \le \frac{\ln x}{x} \le \frac{2}{\sqrt{x}}$ 
Ainsi $\frac{\ln n}{n} \to 0$ par encadrement.
- Donc $\frac{\ln n ^{α }}{n ^{ β }} \to 0$.