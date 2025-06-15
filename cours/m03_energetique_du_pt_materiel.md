# M3: Énergétique du Point Materiel

## Théorème de l'énergie cinétique

$$
m \frac{d\overrightarrow{v}}{dt} \cdot \overrightarrow{v} = \sum_{i} \overrightarrow{f_i} \cdot \overrightarrow{v}
$$

$$
E_c = \frac{1}{2}m v^2
$$

$$
Δ _{AB} E_c = \sum_{i} W_{AB} (\overrightarrow{f_i})
$$

## Forces conservatives et énergie potentielle associé

### Exemple du poids

#### Travail du Poids:
Soit $M ∈ (AB)$ on a $\overrightarrow{g} = -g \overrightarrow{e_z}$

La force $\overrightarrow{P} = m\overrightarrow{g}$

$$
W_{AB}(\overrightarrow{P}) = \overrightarrow{P} . \overrightarrow{AB}
$$

$$
\overrightarrow{P}\left(
    \begin{matrix}
    0 \\ 0 \\ -mg
    \end{matrix}
    \right)
    , \overrightarrow{AB} \left(
        \begin{matrix}
        x_B - x_A \\ y_B - y_A \\ z_B - z_A
        \end{matrix}
        \right)
$$

$$
W_{AB}(\overrightarrow{P}) = -mg(z_B  - z_A)
$$

Le poids est donc une force **conservative** car son travail ne dépend QUE des points $A$ et $B$ et non ps de la trajectoire prise.

#### Énergie potentillle de pesanteur
$$
W_{AB} = -mg(z_B - z_A) \\
= mg(z_A - z_B) \\
= mg z_A - (mg z_B) \\
= (mg z_A + k) - (mg z_B + k) \\
$$

Soit $E_{pp} = mgz + k$
Ainsi $W_{AB}(\overrightarrow{P}) = -(E_{pp}(B) - E_{pp}(A))$

$$
W_{AB}(\overrightarrow{P}) = - Δ _{AB} E_{pp}(M)
$$

#### Définition *Force conservative*

Soit $\overrightarrow{F}$ une force, appliquée au point $M$ entre les points $A$ et $B$.

$\overrightarrow{F}$ est conservative s'il existe une fonction $f(M)$  de la position tel que:
$$
W_{AB}(\overrightarrow{F}) = - Δ _{AB} f(M)
$$

#### Remarque

La constante $K$ est arbitraire donc on la fixe pour l'origine des énergies potentielles.

si $\overrightarrow{g} = -g \overrightarrow{ e_z}$ alors $E_{pp} = mgz + k$

Sinon si $\overrightarrow{g} = g \overrightarrow{e_z}$ alors $E_{pp} = -mgz + k$

### Généralisation: force conservative

Soit $\overrightarrow{F}$ est conservative

$$
∃ E_p(M) / W_{AB}(\overrightarrow{F}) - Δ _{AB} E_p(M)
$$

$$
δ W(\overrightarrow{F}) =- d E_p(M)
$$

$$
\overrightarrow{F} . \overrightarrow{dl} = -d E_p(M) \\
\overrightarrow{F} . \overrightarrow{dl} = -\overrightarrow{\text{grad}}(E_p(M)) . \overrightarrow{dl} \\
\overrightarrow{F} =  -\overrightarrow{\text{grad}}(E_p(M))
$$

#### Exemple
On oriente $z$ vers le haut:
$$
E_p = mgz + k
$$ 

$$
\overrightarrow{\text{grad}}(f) = \left(
    \begin{matrix}
    \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \\ \frac{\partial f}{\partial z}
    \end{matrix}
    \right)_{(\overrightarrow{e_x}, \overrightarrow{e_y}, \overrightarrow{e_z})}
$$

$$
-\overrightarrow{\text{grad}}(mgz+k) = -mg \overrightarrow{e_z} = \overrightarrow{P}
$$

### Force de rappel et énergie potentielle élastique

Soit un ressort de raideur $k$ et longueur a vide $l_0$ orienté selon $\overrightarrow{u_x}$

### Sens physique de l'énergie potentielle

Le travail fourni par l'opérateur pour mettre le système en l'état actuel a partir de l'état de l'origine de l'énergie potentielle.

## Théorème de l'Énergie Mécanique

### Énergie mécanique

Soit $M(m) ∈ \mathcal{E}$ avec une vitesse $\overrightarrow{v}$ subissant les forces $\overrightarrow{f_i}$ parmis lesquelles les forces conservatives $\overrightarrow{F_i}$

On peut associer $E_p(M)$ a $\sum_{i} E_p(\overrightarrow{F_i})$

$$
E_m(M) = E_c(M) + E_p(M)
$$

### Théorème de l'énergie mécanique
$$
Δ _{AB} E_c = \sum_{i} W_{AB}(\overrightarrow{f_i})
$$
$$
Δ _{AB} E_c = \sum_{i} W_{AB}(\overrightarrow{f_{i,nc}}) + \sum_{i} W_{AB}(\overrightarrow{f_{i,c}})
$$
$$
Δ _{AB} E_c = \sum_{i} W_{AB}(\overrightarrow{f_{i,nc}}) - Δ _{AB} E_p(M)
$$
$$
\iff Δ _{AB} E_c + E_p = \sum _{i} W_{AB} (\overrightarrow{f_{i,nc}})
$$
$$
Δ_{AB} E_m = \sum _{i} W_{AB} (\overrightarrow{f_{i,nc}})
$$

#### Exemple: Forces dissipatives

$E_m \searrow \implies Δ E_m < 0 \implies W$ résistant.

### Conservation de l'énergie mécanique

#### Définition *Système conservatif*
Les forces sont soit:
- Conservatives
- Soit elles ne travaillent pas
- Donc $Δ E_m = 0 \implies E_m = k$ 

#### Application




Résolution numérique:
$$
\ddot{ θ } + ω _0 ^2 \sin θ  = 0
$$

On discrétise le temps: $\{t_i\}$

On approxime les valeurs $θ _i \approx \theta (t_i)$

On calcule les valeurs itérativement:
$$
θ _i  \dot{ θ } \implies θ _{i+1} \dot{ θ _{i+1}}
$$

On utilise ensuite un schéma d'Euler
$$
\ddot{ θ } + ω _0 ^2 \sin θ  = 0 \iff \begin{cases}
\dot{ θ } = y \\
\dot{y} = - ω _0 ^2 \sin θ 
\end{cases}
$$

On utilise donc $\dot{ θ } = y(t) =\implies θ (t_{i+1} ) - θ ( t_i) = y(t_i) \times (t_{i+1} - t_i)$

$$
\implies θ _{i+1} = θ _i + y_i \times h
$$

et
$$
\dot{y} = - ω _0 ^2 \sin θ = y_{i+1} - y_i = (- ω _0 ^2 \sin θ _i) \times h
$$

```python
tan
w_0
theta_0
y_0
N = 10000
t = linspace(0, tan, N)
theta = zeros(N)
theta[0] = theta0
y = zeros(N)
y[0] = y_0

for i in range(N-1):
    theta[i+1] = theta[i] + y[i] * h
    y[i+1] = y[i] - w_0**2 * sin(theta[i])*h
```

### Approximation harmonique

Si $θ$ est assez petit alors $\sin θ = θ + \circ ( θ )$

Pour tout système proche d'un état d'équilibre stable, va se mouvoir de maniere très bien approximer par un harmonique.

Soit un système a un degré de liberté, conservatif:
$$
E_p(x)
$$

On suppose $x \sim x_{eq}$
$$
E_p(x) = E_p(x_{eq}) + \overbrace{\frac{\partial E_p}{\partial x}(x_{eq})\ddot{ θ } + ω _0 ^2 \sin θ  = 0
(x - x_{eq})}^{=0} + \frac{1}{2} \frac{\partial^2 E_p}{\partial x^2}(x_{eq})(x-x_{eq})^2
$$

On reconnait la forme de lénergie potentielle élastique.

On aboutie donc a:

$$
E_p(x) = C + \frac{1}{2} m ω _0^2 (x - x_{eq})^2
$$

or
$$
m ω _0 ^2 = \frac{\partial^2 E_p}{\partial x^2}(x_{eq})
$$

$$
ω _0 = \sqrt{\frac{\partial^2 E_p}{\partial x^2}(x_{eq}) \times \frac{1}{m}}
$$


#### Exemple Pendule simple
$$
E_p( θ ) = mg l (1 - \cos θ )
$$
$$
ω _0 = \sqrt{\frac{g}{l}}
$$


