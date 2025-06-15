# Chapitre 32: Variables Aléatoires

#### Théorème

$P_X$ est une probabilité sur l'espace probabilisable $(X( Ω ), \mathcal{P}( X ( Ω )))$ apelée *probabilité image de $P$ par $X$*

#### Preuve

Pour que $P_X$ soit une probabilité on veut:

- $P_X(X( Ω )) = 1$

On a que $P_X( X( Ω )) = P ( X ∈X ( Ω )) = 1$ car certain.

- $P_X( \varnothing) = 0$

$P_X( \varnothing ) = P( X ∈ \varnothing ) = 0$ car impossible.

- $∀A, B ∈\mathcal{P}(X( Ω )) /  A ∩ B = \varnothing, P_X(A ∪B) = P_X(A) + P_X(B)$

Cela donne
$P(X  ∈A ∪ B) = P( X  ∈A) + P(X  ∈B) - P(X ∈A ∩ B)$ or $P(X  ∈A ∩ B = \varnothing) = 0$ donc on a bien la somme.

#### Exemple

- $Ω = \mathfrak{S}_n, | Ω | = n!$
- $∀ ω ∈Ω , P( ω ) = \frac{1}{n!}$


#### Exemple
- $Ω = \{(i, j ) ∈ [[1,n]] \times [[1, i]]\}$
- $P(X = k) = \sum_{i=1}^{n} P_{U_i}(X = k) \times P(U_i)$

$$
P(X = k) = \frac{1}{n} \sum_{i=1}^{n} P_{U_i}(X = k) = \frac{1}{n} \left(\sum_{i=1}^{k-1} 0 + \sum_{i=k}^{n} \frac{1}{i}\right)
$$

$$
\sum_{k=1}^{n} \sum_{i=k}^{n} \frac{1}{in} = \sum_{1 \le k \le i \le n} \frac{1}{in} = \sum_{i=1}^{n} \sum_{k=1}^{i} \frac{1}{in} = \frac{1}{n} \sum_{i=1}^{n} \frac{1}{i} \sum_{k=1}^{i} 1 = \frac{1}{n} \sum_{i=1}^{n} \frac{i}{i} = \frac{n}{n} = 1
$$

#### Théorème

$$
E(X) = \sum_{ ω  ∈Ω } X( ω ) P( \{ ω \}) = \sum_{x ∈X( Ω )} x P(X = x)
$$

#### Preuve

$$
\sum_{ ω ∈ Ω } X( ω  ) P(\{ ω \}) = \sum_{x ∈X( Ω )} \sum_{ ω ∈ Ω  / X( ω ) = x}X( ω ) P(\{ ω \})
$$

$$
= \sum_{x  ∈X( Ω )} \sum_{ ω ∈ Ω / X( ω ) = x} x P(\{ ω \})
$$

$$
= \sum_{x  ∈X( Ω )} x \sum_{ ω ∈Ω / X( ω ) = x} P(\{ ω \})
$$

$$
= \sum_{x  ∈X( Ω )} x P \left(\bigcup_{ ω ∈Ω / X( ω ) = x} \{ ω \} \right)
$$

$$
= \sum_{x  ∈X( Ω )} x P(X = x)
$$
