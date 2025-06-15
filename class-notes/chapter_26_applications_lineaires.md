# Chapitre 26: Applications linéaires

Dans ce chapitre, $E, F, G$ sont des EV

## Généralités sur les Applications linéaires

### Définition

#### Définition *Application Linéaire*

Toute application vérifiant:
1. $∀ x, y  ∈E, f(x+y) = f(x) + f(y)$
2. $∀λ ∈\mathbb{K},  ∀x  ∈E, f(λ x) = λ f(x)$

On note $\mathcal{L}_{\mathbb{K}} (E,F)$

#### Remarque

En particulier, une application linéaires est un morphisme de groupe

et vérifie $f(0) = 0$ 


#### Théorème

"Caractérisation des Applications Linéaires"

Soit $f: E \to F$

$f  ∈\mathcal{L}_{\mathbb{K}}$ si et seulement si:

1. $∀ λ  ∈\mathbb{K},  ∀x, y  ∈E, f( λ x + y) = λ f(x) + f(y)$

2. $∀ λ, μ   ∈\mathbb{K},  ∀x, y  ∈E, f( λ x + μ y) = λ f(x) + μ f(y)$

#### Exemples

$$
f : \mathbb{R} \to \mathbb{R}
$$
$$
x \mapsto ax / a ∈\mathbb{R}
$$

$$
\tilde{\cdot} : \mathbb{K}[X] \to \mathbb{K}[x]
$$
$$
P \mapsto \tilde{P}
$$

$$
z \mapsto \overline{z}, z \mapsto \Re(z), z \mapsto \Im(z)
$$

$$
Σ : \mathbb{K}^{n} \to \mathbb{K}
$$
$$
(a_1, \cdots, a_n) \to \sum_{k=1}^{n} a_k
$$

$$
I ∈C^{0}([a,b], \mathbb{K}) \to \mathbb{K}
$$
$$
f \mapsto \int_a^{b} f(t)dt
$$

#### Définition

On appelle application linéaire de $E$ toute application linéaire de $E$ dans lui-même

Ceci s'appelle un endomorphisme.

noté $\mathcal{L}(E)$

### Opérations sur les applications linéaires

#### Théorème

Si $f ∈\mathcal{L}(E, F), g  ∈\mathcal{L}(F, G)$, alors

$$
g \circ f ∈ \mathcal{L}(E, G)
$$

#### Preuve

Soient $λ  ∈\mathbb{K}, x, y  ∈E$

$g \circ f ( λ x + y) = g( λ f(x) + f(y)) = λ g(f(x)) + g(f(y)) = λ g \circ f (x) + g \circ f(y)$

#### Théorème

Soient $f, g  ∈\mathcal{L}(E,F), λ, μ  ∈\mathbb{K}$

Alors $λ f + μ g  ∈\mathcal{L}(E,F)$

#### Preuve

Soient $x, y ∈E$

Soit $α  ∈\mathbb{K}$
...

#### Théorème

$$
\left(\mathcal{L}(E,F), +, \cdot)\right)
$$

est un EV.

#### Preuve

$$
( F^{E}, +, \cdot) 
$$
est un EV par Caractérisation.

- $\mathcal{L}(E,F) ⊂ F^{E}$
- $\mathcal{L}(E,F) \neq \varnothing$ car l'application nulle y est.

$$
λ f + g  ∈\mathcal{L}(E,F) 
$$


#### Théorème

$$
(\mathcal{L}(E), +, \circ)
$$

Est un anneau

#### Preuve

Montrons que c'est un anneau.

- $(\mathcal{L}(E), +)$ est un groupe abélien

Soient $f,g ∈\mathcal{L}(E), g \circ f  ∈\mathcal{L}(E)$ donc $\circ$ est une LCI.

- $\circ$ est associative sur $\mathcal{L}(E)$ car elle l'est sur $E^{E}$
- $\text{Id}_E ∈\mathcal{L}(E)$ et $∀f  ∈\mathcal{L}(E), f \circ \text{Id}_E = f = \text{Id}_E \circ f$
- Donc $\text{Id}_E$ est le neutre de $(\mathcal{L}(E), \circ)$

- $\circ$ est distributive a droite sur $\mathcal{L}(E)$ car elle l'est sur $E^{E}$.

Soient $f, g, h  ∈\mathcal{L}(E)$ Soit $x ∈ E$.
$$
(f \circ (g +h)) (x) = f((g+h)(x)) = f(g(x) + h(x)) = f(g(x) + f(h(x))
$$

#### Remarque

Dans l'anneau $(\mathcal{L}(E), +, \circ)$ on peut donc appliquer le binome de newton et la généralisation de la 3e identité remarquable.

C'est a dire:
$$
∀ f, g ∈ \mathcal{L}(E) / f \circ g = g \circ f
$$
$$
 ∀n ∈\mathbb{N}, (f+g)^{n} = \sum_{k=0}^{n} \binom{n}{k} f^{k} \circ g^{n-k}
$$
$$
 ∀n  ∈\mathbb{N}, f^{n} - g^{n} = (f - g) \circ \sum_{k=0}^{n-1} f^{k} \circ g^{n-1-k}
$$

#### Remarque

En algèbre linéaire, $f^{k}$ désigne toujours $\bigcirc_{i=0}^{k} f$

### Principe de prolongement d'applications linéaires

#### Théorème

Soient $F, G$ deux SEV supplémentaires de $E$.
I.e.
$$
E = F \oplus G
$$

Soient $u ∈ \mathcal{L}(F, H), v∈\mathcal{L}(G, H)$

Alors il existe une unique application $f  ∈\mathcal{L}(E, H)$

telle que $f_{|F} = u, f_{|G} = v$

#### Preuve

On procède par analyse synthèse

##### Analyse
On suppose donné une telle fonction, on prend un $x$ appartenant a $E$

On sait qu'il existe des uniques $x_1  ∈F$ et $x_2  ∈G$ tel que $x = x_1, x_2$

$$
f(x) = f(x_1 + x_2)
$$

$$
f(x) = f(x_1) + f(x_2)
$$

$$
f(x) = u(x_1) + v(x_2)
$$

##### Synthèse

On pose l'application
$$
f : x \mapsto u(x_1) + v(x_2)
$$

ou $x_1$ et $x_2$ sont les composantes respectives de $F$ et $G$ de la décomposition de $x$.

Comme cette décomposition est unique, $f$ est bien défini.

Soit $x ∈F, y  ∈G$

- $f(x) = u(x) + v(0) = u(x) \implies f_{|F} = u$
- $f(y) = u(0) + v(y) = u(y) \implies f_{|G} = v$

Démontrons maintenant la linéarité de $f$:

Soient $x, y ∈ E / x = x_1 + x_2, y = y_1 + y_2$ avec
$$
x_1,y_1 ∈F, x_2, y_2  ∈G
$$

Soit $λ  ∈\mathbb{K}$ 
$$
f( λ x + y) = f( λ x_1 + λ x_2 + y_1 + y_2)
$$

$$
= u( λ x_1 + y_1) + v( λ x_2 + y_2)
$$

$$
= λ u(x_1) + λ v(x_2) + u(y_1) + v(y_2)
$$

$$
= λ f(x_1 + x_2) + f(y_1 + y_2)
$$

$$
= λ f(x) + f(y)
$$

#### Théorème

On suppose $E$ de dimension finie $n  ∈\mathbb{N}$ 

Soient $\mathcal{B}(e_1, \cdots, e_n)$ une base de $E$

et $\mathcal{F}(f_1, \cdots, f_n)$ une famille de vecteurs de $F$

Il existe une unique application $h  ∈\mathcal{L}(E,F)$ telle que
$$
 ∀1 \le i \le n, h(e_i) = f_i
$$

#### Preuve

On procède par analyse synthèse:

##### Analyse

Soit $h$ une telle application

Soit $x  ∈E$

$$
∃ !( λ _1, \cdots, λ_n) / x = \sum_{k=1}^{n} λ _k e_k
$$


Donc
$$
h(x) = h\left(\sum_{k=1}^{n} λ _i e_i\right) = \sum_{k=1}^{n} λ _i h(e_i) = \sum_{k=1}^{n} λ _i f_i
$$

##### Synthèse

On pose

$$
h x \mapsto \sum_{i=1}^{n} λ _i f_i / x = \sum_{i=1}^{n} λ _i e_i
$$

Les coordonnées de $x$ étant uniques, on a l'unicité de l'application.

Ainsi $f$ est bien définie.


#### Remarque

Une application linéaire est donc uniquement déterminée par l'image d'une base de l'éspace de départ.

### Un nouvel outil pour prouver qu'une partie d'un EV est un SEV

#### Théorème

Soit $f ∈ \mathcal{L}(E,F)$

Si $E'$ un SEV de $E$ alors $f(E')$ est un SEV de $F$

Si $F'$ est un SEV de $F$ alors $f^{-1}(F')$ est un SEV de $E$.

#### Preuve

- $f(E') ⊂F$ et $F$ est un EV
- $0_F ∈f(E')$ donc il est non-vide
- soit $λ  ∈K, a,b ∈f(E')$

Donc $∃ x, y  ∈E'$ tels que $a = f(x), b = f(y)$

$$
λ a + b = λ f(x) + f(y) = f( λ x + y) ∈ f(E')
$$

---

$$
\mathcal{L}(E)^{*} = GL(E)
$$

il est clair que $\mathcal{L}(E)^{*} ⊂ GL(E)$

dans l'autre sens il faut vérifier que si $u  ∈\mathcal{L}(E)$

et si $u$  est bijective alors $u^{-1}  ∈\mathcal{L}(E)$

Soient $x, y  ∈E, λ  ∈\mathbb{K}$ 
$$
u^{-1}( λ x + y) = u^{-1}( λ u(a) + u(b))
$$

Car comme $u$ est surjective $∃ a,b  ∈E / x = u(a), y = u(b)$

$$
u^{-1}(u( λ a + b)) = λ a + b = λ u^{-1}(x) + u^{-1}(y)
$$

## Applications linéaires et familles de vecteurs

### Premières propriétés

#### Théorème

Soit $f  ∈\mathcal{L}(E,F)$ et $\mathcal{L} = (e_i)_{i ∈I}$

une famille de vecteurs de $E$

Si $\mathcal{L}$ est libre et si $f$ est injective alors $f(\mathcal{L})$ est libre.

#### Preuve

Soit $J ⊂ I$ fini.

Soit $( λ _i)_{i  ∈J}$ telque:
$$
\sum λ _i f(e_i) = 0
$$
$$
\implies f( \sum λ _i e_i ) = 0 \text{ car } f \text{ linéaire}
$$

Ainsi
$$
\sum λ _i e_i ∈\text{ker}(f)
$$

Or $f$ est injective donc $\text{ker}(f) = \{0\}$

puis $\sum λ _i e_i = 0$

Or $\mathcal{L}$ est libre donc pour tout $i$, $λ _i = 0$

#### Théorème

Soit $f  ∈\mathcal{L}(E,F)$ et $\mathcal{G} = (e_i)_{i ∈I}$

une famille de vecteurs de $E$

Si $\mathcal{G}$ est génératrice et si $f$ est surjective alors $f(\mathcal{G})$ est génératrice.

#### Preuve

Soit $y  ∈F$

Or $f$ est surjective donc $∃ x  ∈E/ f(x) = y$.

Or $\mathcal{G}$ est génératrice donc:
$$
∃ λ i / i ∈J / x = \sum λ_i e_i
$$

Donc
$$
y = f\left(\sum λ _i e_i\right)
$$

Par linéarité on a:
$$
y = \sum λ _i f(e_i)
$$

#### Corollaire

Soit $f  ∈\text{Isom}(E,F)$

Si $\mathcal{B}$ est une base de $E$ alors

$f(\mathcal{B})$ en est une pour $F$.

#### Corollaire

Soit $f  ∈\text{Isom}(E,F)$,

$E$ est de dimension finie si et seulement si,
$F$ est de dimension finie

et ils ont la même dimension.

#### Théorème

Soit $f  ∈\mathcal{L}(E,F)$ et $\mathcal{B}$ une base de $E$

Si $f(\mathcal{B})$ est une base de $F$ alors $f  ∈\text{Isom}(E,F)$.

#### Preuve

Injectivité:

Soit $x  ∈\text{ker}(f)$

On écrit que $\mathcal{B} = (e_i) / i  ∈I$

comme $\mathcal{B}$ est génératrice on a:
$$
∃ J ⊂I / x = \sum λ _i e_i / i  ∈J
$$

par linéarité:

$$
0 = \sum λ _i f(e_i)
$$

Comme $f(\mathcal{B})$ est une base, elle est libre donc
tous les $λ _i$ sont nuls et $x = 0$

Ainsi $\text{ker}(f) = \{0\}$

Surjectivité:

Soit $y ∈F$

Comme $f(\mathcal{B})$ est génératrice:

$$
∃ J ⊂ I / y = \sum λ _i f(e_i)
$$

Par linéarité:
$$
y = f \left(\sum λ _i e_i\right)
$$

L'antécédent de $y$ est $x = \sum λ _i e_i$

#### Remarques

si $\mathcal{B}$ est juste génératrice elle est forcément une base:

### Dimension de $\mathcal{L}(E,F)$

#### Théorème

On suppose $E,F$ de dimension finie.

Alors:
$$
\text{dim} \mathcal{L}(E,F) = \text{dim} E \times \text{dim} F
$$

#### Preuve

On note $p = \text{dim} E n = \text{dim} F$

Soient $(e_j) / 1 \le j  \le p, (f_i) / 1 \le i \le n$

des bases de $E$ et $F$.

Pour $1 \le i \le n, 1 \le j \le p$ on pose:

l'application linéaire $u_{i,j}$ de $E \to F$ définie par:

$$
∀1 \le k  \le p , u_{i,j} (e_k) = δ _{i,j} f_i
$$

vérifions que $\mathcal{B} = (u_{i,j})$ est une base.

Liberté:

Soit $( λ _{i,j})  ∈\mathbb{K}^{n \times P}$ tels que:

$$
\sum λ _{i,j} u_{i,j} = 0
$$

Soit $1 \le k \le p$. En évaluant en $e_k$ on a:

$$
\sum λ _{i,j} δ _{j,k} f_i = 0
$$

Donc
$$
\sum λ _{i,k} f_i = 0
$$

Par la liberté de $(f_i)$ on a que les $λ _{i,k}$ sont nuls.

Génération:

Soit $u  ∈\mathcal{L}(E,F)$

Soit $1 \le k \le p$.

$u(e_k)  ∈F$ donc

$$
∃ λ _{i,k}  ∈\mathbb{K}^{n}
$$

tels que:
$$
u (e_k) = \sum_{i=1}^{n} λ _{i,k} f_i
$$

$$
u(e_k) = \sum_{i=1}^{n} \sum_{j=1}^{p} λ _{i,j} u_{i,j} (e_k)
$$

$$
u(e_k) = \sum_{i=1}^{n} \sum_{j=1}^{p} λ _{i,j} δ _{j,k} f_i
$$

$$
u(e_k) = \sum_{i=1}^{n} λ _{i,k} f_i
$$

Ainsi:

$$
\sum_{i,j} λ _{i,j} u_{i,j} = u
$$

Car elles ont les mêmes images sur la base et une application linéaire est uniquement determinée par les images d'une base.

Ainsi $\mathcal{B}$ est une base

et $\text{dim} \mathcal{L}(E,F) = |\mathcal{B}| = n \times p$

### Le Théorème du Rang

#### Définition *Rang d'une application*

Soit $f  ∈\mathcal{L}(E,F)$

On appelle rang de $f$ la dimension de $\text{im}(f)$

On note alors $\text{rg}(f)$

#### Exemple

Soit $f  ∈\mathcal{L}(E,F)$.

- $\text{rg}(f) = 0 \iff f = 0$

#### Théorème "Théorème du Rang"

Soit $f  ∈\mathcal{L}(E,F)$

On suppose $E$ de dimension finie.

Alors $\text{ker}(f)$ et $\text{im}(f)$ sont de dimension finie et:

$$
\text{dim} E = \text{dim} (\text{ker}(f)) + \text{rg}(f)
$$

#### Remarque

On A JAMAIS DIT que:
$$
\text{ker}(f) \oplus \text{im}(f) = E
$$

#### Preuve

- $\text{ker}(f)$ est de dimension finie en tant que SEV de $E$ (qui est lui meme fini).

- Soit $S$ un supplémentaire de $\text{ker}(f)$ dans $E$.
- Soit $g$ défini par:

$$
g = f_{|S}^{\text{im}(f)}
$$

$g$ est bien définie et linéaire en tant que restriction d'une applicaitn linéaire.

$$
\text{ker}(g) = \{0\}
$$
car $S \oplus \text{ker}(f) = E$

Donc $y  ∈\text{im}(f)$

Donc $∃ x  ∈E / y = f(x)$

Donc $∃ t  ∈\text{ker}(f) , s  ∈S / x = t+s$ 

Or:
$$
y = f(x) = f(t+s) = f(t) + f(s) = f(s) = g(s)
$$

Donc $∃ s  ∈S / y = g(s)$

et $g$ est surjective.

$g$ est donc un isomorphisme.

d'ou:
$$
\text{dim}(\text{im}(f)) = \text{dim}(S) = \text{dim}(E) - \text{dim}(\text{ker}(f))
$$

#### Remarque

La version officielle du programme est la suivante:

Soit $f  ∈\mathcal{L}(E,F)$

Si $S$ est supplémentaire de $\text{ker}(f)$ dans $E$ alors

$$
f_{|S}^{\text{im}(f)}
$$

est un isomorphisme.

#### Théorème "Théorème d'isomorphisme"

Soit $f  ∈\mathcal{L}(E,F)$ 

On suppose que $E$ et $F$ sont de meme dimension finie.

LASSE:

1. $f$ est un isomorphisme
2. $f$ est injective
3. $f$ est surjective
4. $f$ est inversible a gauche
5. $f$ est inversible a droite

#### Preuve

1. $\implies$ tous les autres points

2 $\implies$ 1:

Par le Théorème du rang, $\text{dim}(E) = \text{dim}(\text{ker}(f)) + \text{rg}(f) = \text{rg}(f) = \text{dim}(\text{im}(f))$

or $\text{im}(f) ⊂F$ et $\text{dim}(\text{im}(f)) = \text{dim} F$

donc $\text{im}(f) = F$

et $f$ est surjective.

3 $\implies$ 1:

D'après le Théorème du rang:

$$
\text{dim}(\text{ker}(f)) = \text{dim}(E) - \text{rg}(f)
$$

or $f$ surjective donc $\text{rg}(f) = \text{dim}F = \text{dim} E$

puis $\text{ker}(f) = \{0\}$

4 $\implies$  2 $\implies$ 1

5 $\implies$ 3 $\implies$ 1

#### Théorème

On suppose $E, F$ de dimension finie. et $f  ∈\mathcal{L}(E,F)$.

Si $f$ est injective alors:
$$
\text{dim} F \ge \text{dim} E
$$

Si $f$ est surjective alors:
$$
\text{dim} E \ge \text{dim} F
$$

#### Preuve

1.
$$
\text{dim} E = \text{dim}(\text{ker}(f)) + \text{rg}(f)
$$

Donc si $f$ est injective alors $\text{dim}(\text{ker}(f)) = 0$

Ainsi:

$$
\text{dim} E = \text{rg}(f) = \text{dim}(\text{im}(f)) \le \text{dim}F
$$

2. 
$$
\text{dim} E = \text{dim}(\text{ker}(f)) + \text{rg}(f)
$$

Or $f$ est surjective donc $\text{rg}(f) = \text{dim}(F)$

puis:
$$
\text{dim} E \ge \text{dim} F
$$

### Propriétés du rang

Dans cette partie $E,F$ sont de dimension finie 

#### Lemme

Soit $f  ∈\mathcal{L}(E,F)$

Soit $A ⊂E$

Alors
$$
\text{Vect}(f(A)) = f(\text{Vect}(A))
$$

#### Preuve

$A ⊂\text{Vect}(A)$ donc $f(A) ⊂f(\text{Vect}(A))$

or $f(\text{Vect}(A))$ est un SEV de $F$

en tant qu'image d'un SEV de $E$ par une application linéaire

Puis $\text{Vect}(f(A))  ⊂f(\text{Vect}(A))$

Soit $y  ∈f(\text{Vect}(A))$

Donc $∃ x  ∈\text{Vect}(A) / y = f(x)$

Donc $∃ e_1, \cdots, e_n ∈A, λ _1, \cdots, λ _n  ∈\mathbb{K} / x = \sum _i λ _i e_i$

- $y = f(x)$
- $y = f\left(\sum_i λ _i e_i\right)$
- $y = \sum λ _i f(e_i)$
- $y ∈\text{Vect}(f(A))$

#### Théorème

Soit $f  ∈\mathcal{L}(E,F)$

Si $e_1, \cdots, e_n$ est une base de $E$ alors:

$$
\text{rg}(f) = \text{rg}(f(e_1), \cdots, f(e_n))
$$

#### Preuve

$$
\text{rg}(f)
$$
$$
= \text{dim}(\text{im}(f))
$$
$$
= \text{dim}(f(E))
$$
$$
= \text{dim}(f(\text{Vect}(e_1, \cdots, e_n)))
$$
$$
= \text{dim}(\text{Vect}(f(e_1), \cdots, f(e_n)))
$$
$$
= \text{rg}(f(e_1), \cdots, f(e_n))
$$

#### Théorème

Soit $f  ∈\mathcal{L}(E,F)$

- $\text{rg}(f) \le \text{dim}E$

avec égalité si et seulement si $f$ est injective

- $\text{rg}(f) \le \text{dim} F$

avec égalité si et seulement si $f$ est surjective

en particulier:
$$
\text{rg}(f) \le \text{min}(\text{dim}E, \text{dim}F)
$$

#### Preuve

- $\text{rg}(f) = \text{dim} E - \text{dim}(\text{ker}(f)) \le \text{dim}(E)$ avec égalité si et seulement si $\text{dim}(\text{ker}(f)) = 0 \iff f$ est injective.


- $\text{rg}(f) = \text{dim}(\text{im}(f)) \le \text{dim} F$

avec égalité si et seulement si $\text{dim}(\text{im}(f)) = \text{dim}(F) \iff f$ est surjective

#### Théorème

Soit $f  ∈\mathcal{L}(E,F)$ et $g  ∈\mathcal{L}(F,G)$

1. Alors $\text{rg}(g \circ f) \le \text{min}(\text{rg}(f), \text{rg}(g))$
2. Si $f$ est surjective alors c'est égal a $\text{rg}(g)$ 
3. Si $g$ est injective alors c'est égal a $\text{rg}(f)$

#### Preuve

- $\text{rg}(g \circ f) = \text{dim}(\text{im}(g \circ f))$
- $= \text{dim}\left((g \circ f)(E)\right)$
- $= \text{dim}(g(f(E)))$

Or $f(E)  ⊂F$ donc $g(f(E)) ⊂ g(F)$

De plus, si $f$ est surjective, on a égalité et $\text{rg}(g \circ f) = \text{rg}(g)$

- $g(f(E)) = \text{im}(g_{|f(E)})$
- $\text{rg}(g \circ f) = \text{dim}(f(E)) - \text{dim}(\text{ker}(g_{|f(E)}))$
- $\le \text{dim}(f(E)) = \text{rg}(f)$

Si de plus $g$ est injective, le coeur est nul et il y a égalité.

#### Exercice

Trouver une CNS sur $f$ pour que $\text{rg}(g \circ f) = \text{rg}(g)$

Trouver une CNS sur $g$ pour que $\text{rg}(g \circ f) = \text{rg}(f)$

#### Corollaire

On ne modifie pas le rang d'une application linéaire en composant celle ci par un isomorphisme.

## Applications linéaires particulières

### Homothéties vectorielles

#### Définition *Homothétie vectorielle*

On dit que $h  ∈E^{E}$ est une Homothétie vectorielle

s'il existe:
$$
λ ∈\mathbb{K} / h = λ \cdot \text{Id}
$$

on parle généralement de $h_ λ$ car $λ$ est unique appelé le rapport de l'homothétie.

#### Théorème

- $∀ λ  ∈\mathbb{K}, h_ λ  ∈\mathcal{L}(E)$
- $∀ λ , μ  ∈\mathbb{K}, h_ μ \circ h_ λ  = h _{ λ \times μ } = h _ λ \circ h _ μ$
- $h _ λ  ∈GL(E) \iff λ \neq 0$
- $h ^{-1}_ λ = h _ {\frac{1}{λ }}$.

### Projections vectorielles

#### Définition *Projection vectorielle*

On suppose que $E \oplus F = G$

On appelle projection vectorielle sur $F$ parallellement a $G$, l'endomorphisme $p$ de $E$ vérifiant:

- $p_{|F} = \text{Id}, p_{|G} = 0$

#### Remarque

L'existence et l'unicité de $p$ résulte su principe de prolongement d'applications linéaires.

- nécéssairement dans cette situation:
- $F = \text{ker}(p - \text{Id})$ et $G = \text{ker}(p)$

Montrons par exemple $G = \text{ker}(p)$

$⊂$ est clair car $p_{|G} = 0$

Soit $x ∈\text{ker}(p) / p(x) = 0$

Comme $E = F \oplus G$ alors $∃ f  ∈F, g  ∈G / x = f+g$

$$
p(x) = p(f+g) = p(f) + p(g) = f \implies f = 0
$$

Donc $x = g \implies x ∈G$

#### Théorème

Si $p$ est une projection vectorielle alors:

$$
p^2 = p
$$

#### Preuve

Soit $x  ∈E$

$∃ f ∈F g ∈G / x = f + g$

$p(x) = f$
$p \circ p(x) = p (p(x)) = p(f) = f = p(x)$

Ainsi
$p^2 = p$

#### Théorème

Soit $p  ∈\mathcal{L}(E)$

si $p^2 = p$ alors:
$$
\text{ker}(p - \text{Id}) = \text{im}(p)
$$

#### Preuve

Soit $x  ∈\text{ker}(p - \text{Id})$

Donc $p(x) = x  ∈\text{im}(p)$

Soit $y  ∈\text{im}(p)$

Donc $∃ x  ∈E / y = p(x)$

$(p - \text{Id}) (y) = p(y) - y = p(y) - p(x) = p(x) - p(x) = 0 \implies y  ∈\text{ker}(p - \text{Id})$

#### Théorème

Soit $p  ∈\mathcal{L}(E)$

si $p^2 = p$

alors $\text{ker}(p - \text{Id}) \oplus \text{ker}(p) = E$

#### Preuve

##### Analyse

On suppose qu'il existe $y  ∈\text{ker}(p - \text{id})$ et $z  ∈\text{ker}(p)$ tel que $x = y + z$

Ainsi
$$
p(x) = p(y) + p(z) = y + 0
$$

Donc
$$
\begin{cases}
y = p(x) \\
z = x - p(x)
\end{cases}
$$

##### Synthèse

On pose $y  ∈\text{p(x)}$ et $z = x - p(x)$

Il est clair que $y + z = x$

or $y  ∈\text{im}(p) = \text{ker}(p - \text{id})$

$$
p(z) = p(x) - p(p(x)) = p(x) - p(x) = 0 \iff z ∈\text{ker}(p)
$$

#### Théorème (résumé)

Soit $p ∈\mathcal{L}(E)$

$p$ est une projection vectorielle, si et seulement si:
$$
p^2 = p
$$

Dans ce cas:
$$
\text{im}(p) = \text{ker}(p - \text{id})
$$
et
$$
E = \text{ker}(p) \oplus \text{ker}(p - \text{id})
$$

#### Remarques

- En général $\text{im}(p)$ et $\text{ker}(p)$ ne sont pas supplémentaires, mais si $p^2 = p$ ils le sont.
- En général dire que $y  ∈\text{im}(p)$ signifie que $∃ x ∈E / y = p(x)$, mais ici $x = y$.
- Dire que $p^2 = p$ signifie que $p$ annulle $X^2 - X = (X-1)X$
- Soit $p / p^2 = p$ on pose $q = \text{id} - p$
$$
q^2 = (\text{id} - p)^2 = id^2 - 2p \circ \text{id} + p^2
$$
$$
q^2 = \text{id} -2p + p = \text{id} - p = q
$$
- si $p$ désigne la projection vectorielle sur $F$ parallellement a $G$ alors $q$ désigne ls projection vectorielle sur $G$ parallellement a $F$ ce qui explique son appellation: **projection vectorielle complémentaire associée a $p$**
- et $qp = pq = 0$
- et $p + q = \text{id}$

#### Exemples

- $\text{id}$ c'est la projection vectorielle sur $E$ parallellement a $\{0\}$
- $0$ c'est la projection vectorielle sur $\{0\}$ parallellement a $E$.
- $\text{Re}, i\text{Im}$ sont des projections vectorielles. dans le $\mathbb{R}-$ev $\mathbb{C}$
- $\text{ent}$ dans $\mathbb{K}-$ev $\mathbb{K}(X)$.

### Symmétrie vectorielle

#### Définition *symmétrie vectorielle*

On suppose que $E = F \oplus G$

On appelle symmétrie vectorielle par rapport a $F$ parallellement a $G$ tout endomorphisme $s$  de $E$ tel que:

$$
s_{|F} = \text{id}, s_{|G} = -\text{id}
$$

#### Remarques

- L'unicité provient du principe de prolongement des applications linéaires.
- On a $F = \text{ker}(s - \text{id})$ et $G = \text{ker}(s + \text{id})$

#### Théorème

Si $s$ est une symmétrie vectorielle alors:
$$
s^2 = \text{id}
$$

#### Preuve

Soit $x  ∈E$ on sait que $∃ f ∈F, g ∈ G / x = f+g$

$$
s^2(x) = s^2(f+g) = s(s(f) + s(g)) = s(f - g) = s(f) - s(g) = f - (-g)  =x
$$

#### Théorème

Soit $s  ∈\mathcal{L}(E)$

Si $s^2 = \text{id}$ alors $E = \text{ker}(s - \text{id}) \oplus \text{ker}(s + \text{id})$

#### Preuve

##### Analyse

On suppose que $y  ∈\text{ker}(s - \text{id})$

et $z  ∈\text{ker}(s + \text{id})$

avec $x = y + z$

$$
s(x) = s(y) + s(z)
$$
$$
s(x) = y - z
$$
$$
\begin{cases}
y = \frac{x+s(x)}{2} \\
z = \frac{x - s(x)}{2}
\end{cases}
$$

##### Synthèse

On pose $y = \frac{x+s(x)}{2}$ et $z = \frac{x - s(x)}{2}$

On remarque que $y+z = x$

or $s(y) = \frac{s(x) + s^2(x)}{2} = \frac{s(x) + x}{2} = y ∈ \text{ker}(s - \text{id})$

et $s(z) = \frac{s(x) - s^2(x)}{2} = \frac{s(x) - x}{2} = -z, z ∈\text{ker}(s + \text{id})$

#### Théorème (résumé)

Soit $s  ∈\mathcal{L}(E)$

Alors $s$ est une symmétrie vectorielle de $E$

si et seulement si
$$
s^2 = \text{id}
$$

Et dans ce cas:
$$
E = \text{ker}(s - \text{id}) \oplus \text{ker}(s + \text{id})
$$

et $s$ est la symmétrie vectorielle de $\text{ker}(s - \text{id})$ parallellement a $\text{ker}(s + \text{id})$

#### Remarques

- Si $s$ est une symmétrie vectorielle alors $s$ anulle le polynome $X^2 - 1 = (X-1)(X+1)$

- si $s' = -s$ alors $s'^2 = s^2 = \text{id}$

- si $s$ désigne la symmétrie vectorielle par rapport a $F$ parallellement a $G$ alors $s'$ désigne ls symmétrie vectorielle par rapport a $G$ parallellement a $F$ ce qui explique son appellation: **symmétrie vectorielle complémentaire associée a $s$**

#### Exemples

- $\top$ est une symmétrie vectorielle en particulier:
$$
M_n(\mathbb{K}) = \text{ker}(\top - \text{id}) \oplus \text{ker}(\top + \text{id)} = S_n(\mathbb{K}) \oplus A_n(\mathbb{K})
$$
- $z \mapsto \overline{z}$ et en particulier:
$$
\mathbb{C} = \text{ker}(\overline{\cdot} - \text{id}) \oplus \text{ker}(\overline{\cdot} + \text{id}) = \mathbb{R} \oplus i\mathbb{R}
$$
- $φ :f \mapsto (x \mapsto f(-x))$ et en particulier:
$$
\mathbb{R}^{\mathbb{R}} = \text{ker}(φ - \text{id}) \oplus \text{ker}(φ + \text{id}) = P(\mathbb{R}) \oplus I(\mathbb{R})
$$ ou $P, I$ correspondent aux fonctions paires et impaires

#### Théorème

Soient $s, p  ∈\mathcal{L}(E)$ tels que $s = 2p - \text{id}$

$s$ est une symmétrie vectorielle si et seulement si,
$p$ est une projection vectorielle.

#### Preuve

$s^2 = \text{id} \iff (2p - \text{id})^2 = \text{id}$

$4p^2 - 4p + \text{id} = \text{id} \iff p^2 = p$ 
