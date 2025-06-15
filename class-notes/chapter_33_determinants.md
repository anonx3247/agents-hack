# Chapitre 33: Déterminants

Dans tout ce chapitre $n  ∈\mathbb{N}, n > 1$, $\mathbb{K} = \mathbb{R} \lor \mathbb{C}$ et $E$ est un $\mathbb{K}-$ev.

## Formes multiplinéaires alternés

#### Théorème

L'image d'une famille liée par une forme $n$-linéaire alternée est nulle

#### Preuve

Soit $φ$ une forme $n$-linéaire alternée sur $E$, et $F = (x_1, \cdots, x_n)$ une famille liée sur $E$.

$∃ i  ∈[1,n] / x_i  ∈\text{Vect}(x_1, \cdots, \hat{x_i}, \cdots, x_n)$

Ainsi $∃ i  ∈[1,n], ∃ ( λ _k)_{k  ∈[1,n] \backslash i} / x_i = \sum_{k  ∈[1,n] \backslash i} λ _k x_k$

Ainsi $φ (x_1, \cdots, x_n) = \cdots$

$$
= \sum_{k  ∈[1,n] \backslash i} λ _k φ (x_1, \cdots, \hat{x_i}, \cdots, x_n)
$$

Donc par l'alternance de $φ$, $φ(x_1, \cdots, x_n) = 0$.

#### Théorème "Action sur une permutation"
Soit $φ$ une forme $n$-linéaire antisymmétrique dur $E$ et $σ  ∈S_n$ et $(x_1, \cdots, x_n)$ une famille de $E$

$$
φ (x_{ σ (1)}, \cdots, x_{ σ (n)}) = ε ( σ ) φ (x_1, \cdots, x_n)
$$

#### Preuve

Soit $φ$ une forme $n$-linéaire antisymmétrique dur $E$ et $σ  ∈S_n$ et $(x_1, \cdots, x_n)$ une famille de $E$

$$
φ (x_{ σ (1)}, \cdots, x_{ σ (n)}) = 
$$

si $σ$ est une transposition $τ = (i, j)$ alors

$φ (x_{ τ (1)}, \cdots, x_{ τ (n)}) = φ (x_1, \cdots, x_{i-1}, x_j, x_{i+1}, \cdots, x_{j-1}, x_i, x_{j+1}, \cdots, x_n)$

$$
= -φ (x_1, \cdots, x_n) = ε ( τ ) φ (x_1, \cdots, x_n)
$$

on pose $σ = \prod_{k=1}^{p} τ _k$

$$
φ (x_{ σ (1)}, \cdots, x_{ σ (n)}) = ε ( τ _1) φ (x_{ τ _2 \cdots τ _p (1)}, \cdots, x_{ τ _2 \cdots τ _p(n)})
$$
$$
\cdots
$$

$$
= φ (x_1, \cdots, x_n) \prod _{k = 1}^{p} ε ( τ _k) = ε ( σ ) φ (x_1, \cdots, x_n)
$$

#### Théorème

Une forme $n$-linéaire est alternée si et seulement si elle est antisymmétrique

#### Preuve

$\impliedby$

Soit $φ$ antisymmétrique, et soit $(x_1, \cdots, x_n)$ une famille liée.
telle que $∃ i < j / x_i = x_j$ alors

$$
φ (x_1, \cdots, x_{i-1}, x_j, x_{i+1}, \cdots, x_{j-1}, x_i, x_{j+1}, \cdots, x_n) = ε (i \text{   } j) φ (x_1, \cdots, x_n) = - φ (x_1, \cdots, x_n)
$$

comme les opposés sont égaux alors c'est nul et $φ$ est alternée.

$\implies$

Soit $φ$ alternée, et soit $(x_1, \cdots, x_n)$ une famille de $E$.

Soit $i < j  ∈[1,n]$.

$$
φ (x_1, \cdots, x_i + x_j, \cdots, x_n) = φ (x_1, \cdots, x_n) + φ (x_1, \cdots, \underbrace{x_j}_\text{a la i-eme place} , \cdots, x_n) = φ (x_1, \cdots, x_n)
$$

par alternance.

En faisant pareil par rapport a la $j-$ieme place on a:

$$
φ (x_1, \cdots, x_{i-1}, x_i + x_j, x_{i+1}, \cdots, x_n) = φ (x_1, \cdots, x_{j-1}, x_i + x_j, x_{j+1}, \cdots, x_n)
$$

Par linéarité:

$$
φ (x_1, \cdots, x_n) + φ (x_1, \cdots, x_{i-1}, x_j, x_{i+1}, \cdots x_n) = φ (x_1, \cdots, x_n) + φ (x_1, \cdots, x_{j-1}, x_i, x_{j+1}, \cdots, x_n)
$$

-- incomplet --

#### Théorème

Le determinant de $E$ de base $\mathcal{B}$ est unique et égal a:
$$
\text{det}(x_1, \cdots, x_n) = \sum_{ σ  ∈S_n} ε ( σ ) \prod_{k=1}^{n} a_{ σ (k),k}
$$

ou
$$
\begin{pmatrix}
a_{1,k} \\ a_{2,k} \\ \vdots \\ a_{n,k}
\end{pmatrix}
$$

Sont les coordonnées de $x_k$ dans $\mathcal{B}$

#### Preuve

On procède par analyse synthèse.

SOit $\mathcal{B} = (e_1, \cdots, e_n)$ une base de $E$.

On suppose que $f$ existe état une forme linéaire ou $f(\mathcal{B}) = 1$ alternée.

Soit la famille $(x_1, \cdots, x_n)  ∈E^{n}$

On décompose la famille dans la base $\mathcal{B}$, on note alors:

$$
 ∀k  ∈[1,n], x_k = \sum_{i = 1}^{n} a_{i,k} e_i
$$

Ainsi

$$
\text{mat}_{\mathcal{B}}(x_k) = \begin{pmatrix}
    a_{1,k} \\ \vdots \\ a_{n,k}
\end{pmatrix}
$$

Montrons la $n-$linéarité.

$$
f(x_1, \cdots, x_n) = f\left( \sum_{i_1=1}^{n} a_{i_1,1}e_{i_1}, \cdots, \sum_{i_n = 1}^{n} a_{i_n,n} e_{i_n}\right)
$$

$$
= \sum_{i_1 = 1}^{n} a_{i_1,1} f\left( e_{i_1}, \sum_{i_2 = 1}^{n} a_{i_2,2} e_{i_2}, \cdots, \sum_{i_n=1}^{n} a_{i_n,n} e_{i_n}\right)
$$

$$
\cdots
$$

$$
= \sum_{j=1}^{n} \sum_{i_j = 1}^{n} a_{i_j,j} f(e_{i_1}, \cdots, e_{i_n})
$$

$$
= \sum_{i_1, \cdots, i_n  ∈[1,n]} \prod_{k=1}^{n} a_{i_k,k} f(e_{i_1}, \cdots, e_{i_n})
$$

Dès que les indices $i_j, i_k,  ∀j,k$ sont égaux le produit est nul car $f$ est alternée, donc:

$$
= \sum_{(i_1, \cdots, i_n)  ∈[1,n]^{n} /  ∀j,k  ∈[1,n], i_j \neq i_k} \prod_{m=1}^{n} a_{i_m,m} f(e_{i_1}, \cdots, e_{i_n})
$$

L'ensemble $|\{(i_1, \cdots, i_n)  ∈[1,n]^{n} /  ∀j,k  ∈[1,n], i_j \neq i_k\}| = |\{ σ / σ  ∈S_n\}|$

Ainsi

$$
f(x_1, \cdots, x_n) = \sum_{ σ  ∈S_n} \prod_{k=1}^{n} a_{ σ (k), k} f(e_{ σ (1)}, \cdots, e_{ σ (n)})
$$

Par le fait que $f$ est une forme $n-$linéaire alternée, elle est antisymmétrique donc on aboutie a:

$$
f(x_1, \cdots, x_n) = \sum_{ σ  ∈S_n} \prod_{k=1}^{n} a_{ σ (k), k} ε ( σ ) f(e_1, \cdots, e_n)
$$

or $f(e_1, \cdots, e_n) = 1$
Donc:

$$
f(x_1, \cdots, x_n) = \sum_{ σ  ∈S_n} ε ( σ )\prod_{k=1}^{n} a_{ σ (k), k}
$$

Synthèse:
Soit 
$$
f(x_1, \cdots, x_n) \mapsto \sum_{ σ  ∈S_n} ε ( σ ) \prod_{k=1}^{n} a_{ σ (k), k}
$$

---

$f$ est donc une forme linéaire sur $E$

Montrons que $f$ est antisymmétrique car alors $f$ seras alternée.

Soit $(x_1, \cdots, x_n)$ on veut montrer que

$$
f(x_1, \cdots x_j, \cdots,x_i, \cdots x_n) = - f(x_1, \cdots, x_i, \cdots, x_j, \cdots, x_n)
$$

Pour $i < j$.

Notons $τ = (i j)$

Donc

$$
f(x_1, \cdots, x_j, \cdots, x_i, \cdots, x_n) = f(x_{ τ (1)}, \cdots, x_{ τ (n)})
$$
$$
= \sum_{ σ ∈ S_n} ε ( σ )\prod_{k=1}^{n} a_{ σ (k), τ (k)}
$$

on effectue le changement d'indice $l = τ (k) \iff k = τ ( l)$ car $τ = τ ^{-1}$

D'ou:

$$
f(x_1, \cdots, x_j, \cdots, x_i, \cdots, x_n) = \sum_{ σ ∈S_n} ε ( σ ) \prod_{l = 1}^{n} a_{ σ τ (l), l}
$$

On pose $θ = σ τ$ or $σ = θ τ ^{-1} = θ τ \iff θ$ et $σ$ sont en bijection sur $S_n$.

$$
= \sum_{ θ   ∈S_n} ε ( θ τ  ) \prod_{l = 1}^{n} a_{ θ (l), l}
$$

$$
= - \sum_{ θ  ∈S_n} ε ( θ ) \prod_{l = 1}^{n} a_{ θ (l), l}
$$

$$
= - f(x_1, \cdots, x_i, \cdots, x_j, \cdots, x_n)
$$

Elle est donc antisymmétrique et donc alternée.


#### Remarque

$$
 ∀f, n-\text{linéare alternée sur } E,  ∀(x_1, \cdots, x_n), f(x_1, \cdots, x_n) = f(e_1, \cdots, e_n) \cdot \text{det}_{(e_1, \cdots, e_n)}(x_1, \cdots, x_n)
$$

Donc
$$
 ∀f, n-\text{linéaire alternée sur } E, ∃ λ  / f = λ \cdot \text{det} 
$$

Ainsi $Λ _n^{*}(E) ⊂ \text{Vect}(\text{det})$

$$
\text{dim} \text{Vect} ( \text{det}) = 1 \text{ car } \text{det} \neq Θ 
$$

Soit $f ∈\text{Vect}( \text{det})$ donc $∃ λ  ∈\mathbb{K} / f = λ . \text{det}$.

Or $\text{det}$ est une fomre $n$-linéaire alternée.

Soit $i  ∈[1,n], (x_1, \cdots, x_{i-1}, x_{i+1}, \cdots, x_n)$ Soit $α  ∈\mathbb{K}$et $x_i, y_i$ deux vecteurs de $E$.

$$
f(x_1, \cdots, x_{i-1}, α x_i + y_i, x_{i+1}, \cdots, x_n) = λ . \text{det} (x_1, \cdots, x_{i-1}, α x_i + y_i, x_{i+1}, \cdots, x_n)
$$

$$
= α λ \text{det}(x_1, \cdots, x_n) + λ \text{det} (x_1, \cdots, x_{i-1}, y_i, x_{i+1}, \cdots, x_n)
$$

$$
= α f(x_1, \cdots, x_n) + f(x_1, \cdots, x_{i-1}, y_i, x_{i+1}, \cdots, x_n)
$$

Donc $f$ est une forme $n$-linéaire.

Soit $x_1, \cdots, x_n$ avec $i \neq j$ tels  que $x_i = x_j$

alors
$$
f(x_1, \cdots, x_n) = λ \text{det}(x_1, \cdots, x_n) = 0
$$

Elle est donc alternée.

Ainsi $Λ _n^{*} = \text{Vect}( \text{det})$

#### Théorème

Soient $B, B'$ deux bases de $E$.
Soient $(x_1, \cdots, x_n) ∈E^{n}$

Alors

$$
\text{det}_B(x_1, \cdots, x_n) = \text{det}_B(B') \times \text{det}_{B'} (x_1, \cdots, x_n)
$$

#### Preuve

$$
Λ _n^{*} = \text{Vect}(\text{det}_B) = \text{Vect}(\text{det}_{B'})
$$

Donc $∃ λ ∈\mathbb{K} / \text{det}_B = λ \text{det}_{B'}$

D'ou:

$$
\text{det}_B(B') = λ \text{det}_{B'}(B') \iff λ = \text{det}_{B}(B')
$$

Et on a

$$
\text{det}_B = \text{det}_b(B') \text{det}_{B'}
$$

#### Théorème

Soit $F$ une famille de $E$
$$
\text{det}(B) \neq 0 \iff F \text{ est une base}
$$

#### Théorème

Soit $f ∈\mathcal{L}(E)$ on note alors $\text{det}(f)$:
$$
 ∀φ  ∈Λ _n^{*}(E), ∀ (x_1, \cdots, x_n) ∈ E^{n}, φ (f(x_1), \cdots, f(xn)) = \text{det}(f)\cdot φ (x_1, \cdots, x_n)
$$

#### Preuve

Soit $f ∈\mathcal{L}(E)$

Soit $φ  ∈Λ _n ^{*}(E)$ non nul, alors on a $Λ _n^{*}(E) = \text{Vect}( φ )$

Soit $ψ ∈Λ _n ^{*}(E)$ non nul alors $Λ _n^{*}(E) = \text{Vect}( ψ )$

Notons:
$$
φ _f : (x_1, \cdots, x_n) \mapsto φ (f(x_1), \cdots, f(x_n))
$$

$$
ψ _f : (x_1, \cdots, x_n) \mapsto ψ (f(x_1), \cdots, f(x_n))
$$

Soient $x_1, \cdots, x_n, y_i  ∈E, λ  ∈\mathbb{K}$

$$
φ_f(x_1, \cdots, x_{i-1}, λ x_i + y_i, x_{i+1}, \cdots, x_n) = φ (f(x_1), \cdots, f(x_{i-1}), f(λ x_i + y_i), f(x_{i+1}), \cdots, f(x_n))
$$

Par linéarité de $f$ on a:

$$
φ_f(x_1, \cdots, x_{i-1}, λ x_i + y_i, x_{i+1}, \cdots, x_n) = φ (f(x_1), \cdots, f(x_{i-1}), λ f(x_i) + f(y_i), f(x_{i+1}), \cdots, f(x_n))
$$

Par linéarité de $φ$ on a:

$$
φ_f(x_1, \cdots, x_{i-1}, λ x_i + y_i, x_{i+1}, \cdots, x_n) = λ φ (f(x_1), \cdots,f(x_n)) + φ (f(x_1), \cdots, f(x_{i-1}), f(y_i), f(x_{i+1}), \cdots, f(x_n))
$$

Donc $φ_f, ψ_f$ sont $n-$linéaires.

Soient $x_1, \cdots, x_n i<j / x_i = x_j$

Alors $f(x_i) = f(x_j)$

D'ou:

$$
φ_f(x_1, \cdots, x_i, \cdots, x_j, \cdots, x_n) = φ (f(x_1), \cdots, f(x_i), \cdots, f(x_j), \cdots, f(x_n))
$$

$$
= φ (f(x_1), \cdots, f(x_j), \cdots, f(x_i), \cdots, f(x_n)) = φ _f(x_1, \cdots, x_j, \cdots, x_i, \cdots, x_n)
$$

Donc $φ _f, ψ _f$ sont alternées.

Ainsi $φ_f  ∈\text{Vect}( φ ), ψ _f ∈\text{Vect}( ψ )$

D'ou ,$∃ μ / φ _f = μ φ$ et $∃ ν / ψ _f = ν ψ$

On sait que $∃ α / ψ = α φ$

Donc

$$
ψ _f = ν α φ
$$

$$
ψ _f(x_1, \cdots, x_n) = ψ (f(x_1), \cdots, f(x_n)) = α φ (f(x_1), \cdots, f(x_n)) = α φ _f(x_1, \cdots, x_n)
$$

D'ou $ψ _f = α φ _f$

On a donc:
$$
\begin{cases}
ψ _f = ν α φ \\
ψ _f = α φ _f = α μ φ
\end{cases}
$$

Ainsi $α ( μ - ν ) φ = 0$

$ψ \neq 0$ donc $α \neq 0$

et $φ \neq 0$ donc
$$
μ = ν
$$

Donc $E λ  ∈\mathbb{K} / ∀ φ  ∈Λ _n^{*}(E), φ (f(x_1), \cdots f(x_n)) = λ φ (x_1, \cdots, x_n)$

Donc en particulier, pour $φ = \text{det}$ dans une base quelconque

$$
λ = \text{det}(f(e_1), \cdots, f(e_n))
$$

Avec cela vraie pour toute base $(e_1, \cdots, e_n)$.

#### Théorème

Soient $f,g  ∈\mathcal{L}(E)$ alors

$$
\text{det}(fg) = \text{det}(f)\text{det}(g)
$$

#### Preuve

Soit une base $(e_1,\cdots, e_n)$

$$
\text{det}(fg) = \text{det}(fg(e_1), \cdots, fg(e_2))
$$

$$
= \text{det}(f) \cdot \text{det} (g(e_1), \cdots, g(e_n))
$$
$$
= \text{det}(f) \cdot \text{det}(g)
$$

#### Théorème

Soit $f  ∈\mathcal{L}(E)$ alors

$$
f  ∈GL(E) \iff \text{det}(f) = 0
$$

Et dans ce cas
$$
\text{det}(f^{-1}) = \frac{1}{\text{det}(f)}
$$

#### Preuve

Soit une base $(e_1, \cdots, e_n)$

$f  ∈GL(E) \iff (f(e_1), \cdots, f(e_n))$ est une base.
$$
\iff \text{det}(f(e_1), \cdots, f(e_n)) \neq 0 \iff \text{det}(f) \neq 0
$$

On sait que $\text{det}(\text{id}) = 1$

Donc
$$
\text{det}(f f^{-1}) = 1 = \text{det}(f) \text{det}(f^{-1}) \iff \text{det}(f^{-1}) = \frac{1}{\text{det}(f)}
$$

#### Théorème

Si $A = (a_{i,j})_{[n]}, \text{det}(A) = \prod_{i=1}^{n} a_{i,i}$

Pour $1 \le j < i \le n, a_{i,j} = 0$

$$
\text{det}(A) = \sum_{ σ  ∈S_n} ε ( σ ) \prod_{k=i}^{n} a_{ σ (k), k}
$$

$$
= \sum_{ σ ∈S_n / σ (k) \le k} \prod_{k=1}^{n} a_{ σ (k), k}
$$

checrchons ces permutations:

Si $∀k  ∈[1,n], σ (k) \le k$ alors $I( σ ) = 0 \iff σ = \text{id}$

Donc
$$
\text{det}(A) = \prod_{k=1}^{n} a_{k,k}
$$

Si c'est inferieur le raisonnement est analogue.

#### Théorème

Soit $(x_1, \cdots, x_n) ∈E^{n}$ alors
$$
\text{det}(x_1, \cdots, x_n) = \text{det}(\text{mat}(x_1, \cdots, x_n))
$$

Soit $f  ∈\mathcal{L}(E)$ alors

$$
\text{det}(f) = \text{det}(\text{mat}(f))
$$

#### Théorème

$$
A,B  ∈M_n(\mathbb{K}), \text{det}(AB) = \text{det}(A)\text{det}(B)
$$

#### Preuve

Considérons $f,g$ les endomorphismes canoniquemnet associées a $A$ et $B$.

$$
A = \text{mat}(f); B = \text{mat}(g)
$$

dans la base canonique de $\mathbb{K}^{n}$

D'ou
$$
AB = \text{mat}(fg)
$$

$$
\text{det}(AB) = \text{det}(fg) = \text{det}(f)\text{det}(g) = \text{det}(A)\text{det}(B)
$$

#### Théorème

$$
A ∈ GL_n(\mathbb{K}) \iff \text{det}(A) \neq 0
$$

Et dans ce cas

$$
\text{det}(A^{-1}) = \frac{1}{\text{det}(A)}
$$

#### Preuve

$$
A  ∈GL_n(\mathbb{K}) \iff f  ∈GL(\mathbb{K}^{n}) / A = \text{mat}(f)
$$

$$
f ∈GL(\mathbb{K}^{n}) \iff \text{det}(f) \neq 0 \iff \text{det}(A) \neq 0
$$

Et ici on a bien
$$
\text{det}(A^{-1}) = \frac{1}{\text{det}(A^{-1})}
$$

#### Théorème

$\text{det}$ est un morphisme de groupes de $(GL_n(\mathbb{K}),\times )$ dans $(\mathbb{K}^{*}, \times)$

#### Théorème

$$
\text{det}(A) = \text{det}(A^{T})
$$

#### Preuve
Soit $A = (a_{i,j})  ∈M_n(\mathbb{K})$ et $B = A^{T}, B = (b_{i,j}$

Et on a $b_{i,j} = a_{j,i}$.

Par définition:
$$
\text{det}(A^{T}) = \sum_{ σ  ∈S_n} ε ( σ ) \prod_{k=1}^{n} b_{ σ (k), k} = \sum_{ σ  ∈S_n} ε ( σ ) \prod_{k=1}^{n} a_{ k, σ (k)}
$$

on pose $l = σ (k) \iff k = σ ^{-1}(l)$

$$
\text{det}(A^{T}) = \sum_{ σ ∈S_n} ε ( σ ) \prod_{l=1}^{n} a_{ σ ^{-1}(l), l}
$$

$$
\text{det}(A^{T}) = \sum_{ σ ∈S_n} ε ( σ^{-1} ) \prod_{l=1}^{n} a_{ σ ^{-1}(l), l}
$$

l'application $σ \mapsto σ ^{-1}$ est une bijection de $S_n$ donc on change l'indice de $σ ^{-1}$ a $σ$:

$$
\text{det}(A^{T}) = \sum_{ σ  ∈S_n} ε ( σ ) \prod_{k=1}^{n} a_{ σ (k), k} = \text{det}(A)
$$

#### Théorème

Soit $A  ∈M_n(\mathbb{K})$, on note  $A_{ij}$ la matrice qui est $A$ sans la $i$-eme ligne et sans la $j-$ieme colonne. Ainsi $A_{ij} ∈ M_{n-1}(\mathbb{K})$.

On note $Δ _{ij} = \text{det}(A_{ij})$ le *mineur d'indice $(i,j)$

Et $(-1)^{i+j} Δ _{ij}$ le *cofacteur d'indice* $(i,j)$.

$$
\text{det}(A) = \sum_{i =1}^{n} a_{ij} (-1)^{i+j} Δ _{ij}
$$

#### Preuve

On note $A = (C_1, \cdots, C_n)$ et $B = (E_1, \cdots, E_n)$ la base canonique de $M_n(\mathbb{K})$.

$$
C_j = \sum_{i=1}^{n} a_{ij} E_i
$$

$$
\text{det}(A) = \text{det}_B(C_1, \cdots, C_n) = \text{det}_B(C_1, \cdots, C_{j-i}, \sum_{i=1}^{n} a_{ij} E_i, C_{j+1}, \cdots, C_n)
$$

Par $n-$linéarité de $\text{det}_B$ on a:

$$
\text{det}(A) = \sum_{i=1}^{n} a_{ij} \text{det}_B (C_1, \cdots, C_{j-1}, E_i, C_{j+1}, \cdots, C_n)
$$

On permute succésivement les colonnes $j$ et $j+1$, $j+1$ et $j+2$, $\cdots$ $n-1$ et $n$.

Par antisymmétrie du déterminant on obtient

$$
\text{det}(C_1, \cdots, C_{j-1}, E_i, C_{j+1}, \cdots, C_n) = (-1)^{n-j} \text{det}(C_1, \cdots, C_{j-1}, C_{j+1}, \cdots, C_{n-1}, C_n, E_i)
$$

$$
= (-1)^{n-j}\begin{vmatrix}
a_{11} & \cdots & a_{1,j-1} & a_{1,j+1} & \cdots & a_{1n} & 0 \\
\vdots &        &           &           &              &   & \vdots \\
a_{i1} &        &           &           &        &        & 1 \\
\vdots &        &           &           &               &  & \vdots \\
a_{n1} & \cdots & a_{n,j-1} & a_{n,j+1} & \cdots & a_{nn} & 0 \\
\end{vmatrix}
$$

On permute successivement les lignes $i$ et $i+1$, $i+1$ et $i+2$, $\cdots$ $n-1$ et $n$


$$
= (-1)^{n-j}(-1)^{n-i}\begin{vmatrix}
a_{11} & \cdots & a_{1,j-1} & a_{1,j+1} & \cdots & a_{1n} & 0 \\
\vdots &        &           &           &            &     & \vdots \\
a_{i-1,1} &        &           &           &        &        & 0 \\
a_{i+1,1} &        &           &           &        &        & 0 \\
\vdots &        &           &           &             &    & \vdots \\
a_{n1} & \cdots & a_{n,j-1} & a_{n,j+1} & \cdots & a_{nn} & 0 \\
a_{i,1} &        &           &           &        &        & 1 \\
\end{vmatrix}
$$

$$
= (-1)^{n-i}(-1)^{n-j}\begin{vmatrix}
a_{11} & \cdots & a_{1,j-1} & a_{1,j+1} & \cdots & a_{1n} \\
\vdots &        &           &           &         & \\
a_{i-1,1} &        &           &           &        &         \\
a_{i+1,1} &        &           &           &        &        \\
\vdots &        &           &           &                & \vdots \\
a_{n1} & \cdots & a_{n,j-1} & a_{n,j+1} & \cdots & a_{nn}  \\
\end{vmatrix}
$$

$$
= (-1)^{2n-(i+j)} Δ_{ij}
$$


La $i-$ieme ligne de $A$ est la $i-$eme colonne de $A^{T}$ donc:
$$
\text{det}(A^{T}) = \sum_{j=1}^{n} b_{j,i} (-1)^{i+j} \text{det}( (A^{T})_{ij})
$$

$$
(A^{T})_{ij} = (A_{ij})^{T}
$$

$$
\text{det}(A) = \text{det}(A^{T}) = \sum_{j=1}^{n} a_{ij} (-1)^{i+j} \text{det}(A_{ij})
$$
$$
\text{det}(A) = \sum_{j=1}^{n} a_{ij} (-1)^{i+j} Δ _{ij}
$$

$$
\frac{a}{b} | 3x^2 
$$

#### Théorème "Formules de Cranner"

Soit $A ∈GL_n(\mathbb{K})$ et $B ∈M_{n,1}(\mathbb{K})$

L'unique solution $X = \left(\begin{matrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{matrix}\right)$

du système $AX = B$ et donnée par:

$$
 ∀ i  ∈[1,n], x_i = \frac{\text{det}(C_1, \cdots, C_{i-1}, B, C_{i+1}, \cdots, C_n)}{\text{det}(A)}
$$

#### Preuve

$$
\text{det}_B(A) = (C_1, \cdots, C_n)
$$

ou $B$ est la base canonique de $M_{n,1}(\mathbb{K})$

On a:

$$
\text{det}(C_1, \cdots, C_{i-1}, B, C_{i+1}, \cdots, C_n) = \text{det}(C_1, \cdots, C_{i-1}, \sum_{j=1}^{n} x_jC_j, C_{i+1}, \cdots, C_n)
$$
Par linéarité on a:

$$
= \sum_{j=1}^{n} x_j \text{det}(C_1, \cdots, C_{i-1}, C_j, C_{i+1}, \cdots, C_n)
$$


par alternance on a:
$$
= x_i \text{det}(C_1, \cdots, C_{i-1}, C_i, C_{i+1}, \cdots, C_n)
$$

$$
= x_i \text{det}(A)
$$

D'ou:

$$
x_i = \frac{\text{det}(C_1, \cdots, C_{i-1}, B, C_{i+1}, \cdots, C_n)}{\text{det}(A)}
$$

#### Exemple

Resoudre le système:

$$
(S):\begin{cases}  ax + by = c  \\  a'x + b'y = c' \end{cases}
$$

son déterminant vaut: $\text{det}(S) = ab' - a'b$:

$$
 \left|\begin{matrix} a & b \\ a' & b' \end{matrix}\right|
$$

Donc

$$
x = \frac{ \left|\begin{matrix} c & b \\ c' & b' \end{matrix}\right| }{ab'-a'b
}$$

$$
y = \frac{ \left|\begin{matrix} a & c \\ a' & c' \end{matrix}\right| }{ab'-a'b
}$$

On remplace le membre qu'on veut connaitre par la solution.

#### Exemple

$$
\begin{cases} x + y + z = 1 \\  ax + by + cz = d \\  a^2x + b^2y + c^2z = d^2 \end{cases}
$$

D'après vandermonde on a:
$$
 \left|\begin{matrix} 1 & 1 & 1 \\ a & b & c \\ a^2 & b^2 & c^2 \end{matrix}\right| = (b-a)(c-b)(c-a)
$$

Ce système est de Cranner si et seulement si $| \{a,b,c\}| = 3$

Dans ce cas:

$$
x = \frac{ \left|\begin{matrix} 1 & 1 & 1 \\ d & b & c \\ d^2 & b^2 & c^2 \end{matrix}\right| }{\left(b-a\right)\left(c-b\right)\left(c-a\right)
}$$

$$
y = \frac{ \left|\begin{matrix} 1 & 1 & 1 \\ a & d & c \\ a^2 & d^2 & c^2 \end{matrix}\right| }{\left(b-a\right)\left(c-b\right)\left(c-a\right)
}$$

$$
z = \frac{ \left|\begin{matrix} 1 & 1 & 1 \\ a & b & d \\ a^2 & b^2 & d^2 \end{matrix}\right| }{\left(b-a\right)\left(c-b\right)\left(c-a\right)
}$$

$$
\begin{cases}  x = \frac{\left(b-d\right)\left(c-d\right)}{\left(b-a\right)\left(c-a\right)}  \\  y = \frac{\left(d-a\right)\left(c-d\right)}{\left(b-a\right)\left(c-b\right)}  \\  z = \frac{\left(d-b\right)\left(d-a\right)}{\left(c-b\right)\left(c-a\right)} \end{cases}
$$

#### Théorème

On note la comatrice de $A  ∈M_n(\mathbb{K})$:
$$
\text{com}(A) = ( (-1)^{i+j}Δ _{i,j} )_{i,j}
$$

Et on a

$$
A \text{com}(A)^{T} = \text{com}(A)^{T} A = \text{det}(A) I_n
$$

$$
\text{com}(\text{com}(A)) = A
$$

$$
A = \left( \begin{matrix} a & b \\ c & d \end{matrix}\right) \left(\begin{matrix} d & -c \\ -b & a \end{matrix} \right), \text{com}\left(\text{com}\left(A\right)\right) = A
$$

#### Preuve

Montrons que $\text{com}(A)^{T} A = \text{det}(A) I_n$

On note $(-1)^{i+j}, Δ _{ij} = M_{ij}$

Soient $1 \le i,j \le n$

$$
(\text{com}(A)^{T}A)_{ij} = \sum_{k=1}^{n} M_{k,i} a_{k,j}
$$

par developpement de la colonne $j$:


Si $i \neq j$ en developpant selon la colonne $i$ le determinant suivant:

$$
 \left|\begin{matrix}  a_{11} &  \cdots &  a_{1j} &  \cdots &  a_{1j} &  \cdots &  a_{1n} \\  \vdots &   &  \vdots &   &  \vdots &   &  \vdots \\  a_{n1} &  \cdots &  a_{nj} &  \cdots &  a_{nj} &  \cdots &  a_{nn}  \end{matrix}\right| = 0 = \sum_{k=1}^{n} a_{ik} M_{ki}
$$

Il s'agit de la matrice $A$ a laquelle on a remplacé la colonne $i$ par $j$.

$$
= \begin{cases}  \det\left(A\right)  &  \text{si } i = j  \\  X  &  \text{si } i \neq j  \end{cases}
$$

## Caractérisation du rang a l'aide du determinant

#### Définition *Matrice extraite*

Toute matrice obtenue a partir d'une matrice $A  ∈M_{n,p}(\mathbb{K})$ en lui retirant des lignes et/ou des colonnes.

#### Exemple

$$
\left(\begin{matrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{matrix}\right)
$$

est extraite de:

$$
\left(\begin{matrix} 1 & 2 & 3 & 10 \\ 4 & 5 & 6 & 11 \\ 7 & 8 & 9 & 12 \end{matrix}\right)
$$

en lui enlevant la dernière colonne.

#### Théorème

Soit $A  ∈M_{n,p}(\mathbb{K})$

Toute les matrices extraites de $A$ lui sont de rang inférieur.

#### Preuve

clair.

#### Définition *Determinant extrait*

On appelle determinant extrait d'une matrice $A  ∈M_{n,p}(\mathbb{K})$ tout déterminant d'une matrice carée extrait de $A$.

#### Exemple

Soit $A  ∈M_n(\mathbb{K})$ 
Les determinants extraits de taille $n-1$ de $A$ sont les mineurs de $A$.

#### Théorème "Caractérisation du rang a l'aide du déterminant"

Soit $A  ∈M_{n,p}(\mathbb{K})$ On suppose $A \neq 0$

- Le rang de $A$ est égal a la taille de la plus grande matrice inversible extraite de $A$.

- Le rang est égal a la taille du plus grand déterminant extrait de $A$ non nul.

#### Exemple

Soit $A  ∈M_n(\mathbb{K})$

- $\text{rg}(A) = n \iff \text{det}(A) \neq 0$
- $\text{rg}(A) = n-1 \iff \text{det}(A) = 0$ et $∃ i, j  ∈[1,n] / Δ _{i,j} \neq 0$.

Soit $1 \le r \le n-1$ alors

$\text{rg}(A) = r \iff$ il existe une matrice extraite de $A$  inversible de taille $r$ et toutes les matrices extraites plus grandes ont un determinant plus grand.


En fait il suffit de montrer que le determinant est nul pour les matrices extraites de taille $r+1$


#### Exemple

$$
\left(\begin{matrix} 1 & 1 & 0 & \cdots & 0 \\ \ddots & \ddots & \ddots & \cdots & \vdots \\ 0 & \cdots & \cdots & 1 & 1 \\ 0 & \cdots & \cdots & 0 & 1 \\ 1 & \cdots & \cdots & \cdots & 1 \end{matrix}\right)
$$

$$
\det A = \left|\begin{matrix} 1 & 1 & \cdots & 0 \\  & \vdots & \vdots &  \\ 0 & \cdots &  & 1 \end{matrix}\right| + \left|\begin{matrix} 0 & 1 & \cdots & 0 \\ \vdots \\ 0 & 0 & \cdots & 1 \\ 1 & 0 & \cdots & 1 \end{matrix}\right| $$

(en developpant la 1ere colonne)

$$
= 1 + (-1)^{n+1} \times 1 \times |A|_{n-1}
$$

$$
= 1 + (-1)^{n+1}
$$

Si $n$ est impair alors $\det A = 2$ donc $\text{rg}(A) = n$ sinon $\text{rg}(A) \neq n$ et $Δ _{n,1} \neq 0$ donc $\text{rg}(A) = n-1$

Si $\text{rg}(A) \le n-1,$ alors $∀i,j, Δ _{ij} = 0$

Donc $\text{com}(A) = 0$

Si $\text{rg}(A) = n-1$ alors $∃i,j / Δ _{ij} \neq 0 =\implies\text{rg}(\text{com}(A)) \ge 1$

Si $\text{rg}(A) = n$ alors $A  ∈GL_n(\mathbb{K})$

On a $\text{com}(A)^{T} A = \text{det}(A) I_n$

Donc

$$
\text{com}(A)^{T} \times (\frac{1}{\text{det}A} A) = I_n
$$

Donc $\text{com}A  ∈GL_n(\mathbb{K})$

et $\text{rg}(\text{com}(A)) = n$

Si $\det A = 0$ on a:

$$
\text{com}(A)^{T} A = 0
$$

donc $\text{im}(A) ⊂\text{ker}(\text{com}(A)^{T})$

d'ou:

$$
\text{rg}(A) \le \text{dim}(\text{ker}(\text{com}(A)^{T})) = n - \text{rg}(\text{com}(A)^{T})
$$

$$
\text{rg}(A) \le n - \text{rg}(\text{com}(A))
$$

$$
n-1 \le n - \text{rg}(\text{com}(A))
$$

$$
\text{rg}(\text{com}(A)) \le 1
$$

or $\text{rg}(\text{com}(A)) \ge 1$ donc il y a égalité.


