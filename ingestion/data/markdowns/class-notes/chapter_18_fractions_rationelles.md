# Chapitre 18: Fractions Rationelles

$$
F = \frac{1}{(X^2+X+1)(X+1)^2}
$$

$\text{deg}(F) = -4 < 0$

dons la partie entierre de $F$ est nulle

- $F = \frac{aX+b}{X^2+X+1} + \frac{c}{X+1} + \frac{d}{(X+1)^2}$

### Calcul de $d$

On multiplie par $(X+1)^2$ et on evalue en $-1$ on a: $d = 1$

### Calcul de $c$ 

On multiplie par $(X+1)^2$ on dérive et on évalue en $-1$, on a:
$$
c = \frac{d}{dx} (\frac{1}{x^2+x+1}) = \frac{-(2x+1)}{(x^2+x+1)}
$$

$c = 1$

### Calcul de $a$ et $b$

En évaluant en $0$ on a:
$$
F = 1 = b + c+ d \iff b = -1
$$

On multiplie par $X$ et on passe a la limite en $+\infty$

$$
F = \frac{aX^2+bX}{X^2+X+1} + \frac{cX}{X+1} + \frac{dX}{(X+1)^2}
$$

$$
0 = a + c \iff a = -1
$$

$$
\frac{1}{(X^2+X+1)(X+1)^2} = \frac{-X-1}{X^2+X+1} + \frac{1}{X+1} + \frac{1}{(X+1)^2}
$$


#### Une technique efficace

#### Théorème

Soit $F = \frac{P}{Q} ∈ \mathbb{K}(X)$ une fraction rationelle, et $a ∈ \mathbb{K}$ on suppose que $a$ est pole simple de $F$

Le coefficient de la décomposition en elements simples de $F$ dans $\mathbb{K}(X)$ qui apparait devient $\frac{1}{X - a}$ et est egal a:
$$
\frac{\tilde{P}(a)}{\tilde{Q'}(a)}
$$

#### Un dernier resultat

#### Théorème

Soit $P = λ \times \prod_{k=1}^{r}(X - a_k)^{m_k} ∈ \mathbb{K}[X]$

un polynome scindé

alors $\frac{P'}{P} = \sum_{k=1}^{r} \frac{m_k}{X - a_k}$ est c'est la decomposition en elements simples de $\frac{P'}{P}$ dans $\mathbb{K}(X)$

$$
\text{deg}(F_1 + F_2) \le \text{max}(\text{deg}(F_1), \text{deg}(F_2))
$$
avec égalité si $\text{deg}(F_1) \neq \text{deg}(F_2)$



- Idempotence de $i$ pour 5
- pivot de gauss = operation elementaires des matrices
- q
