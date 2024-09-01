# Model API

You can write your own models, that are compatible with the utils and calculators in this package, or elsewhere.
All models must inherit the base class finmc.models.base.MCBase

::: finmc.models.base

## Example

```py
# Define a single asset Black Scholes process with a flat volatility
class BSMC(MCFixedStep):
    def reset(self):
        # fetch the model parameters from the dataset
        ...

        # Initialize rng and any arrays
        self.rng = Generator(SFC64(self.dataset["MC"].get("SEED")))
        self.x_vec = np.zeros(self.n)  # process x (log stock)
        self.cur_time = 0

    def step(self, new_time):
        """Update x_vec in place when we move simulation by time dt."""

        dt = new_time - self.cur_time
        fwd_rate = self.asset_fwd.rate(new_time, self.cur_time)

        dz_vec = self.rng.standard_normal(self.n) * sqrt(dt) * self.vol
        self.x_vec += (fwd_rate - self.vol * self.vol / 2.0) * dt + dz_vec

        self.cur_time = new_time

    def get_value(self, unit):
        """Return the value of the modeled asset at the current time."""
        if unit == self.asset:
            return self.spot * np.exp(self.x_vec)

    def get_df(self):
        return self.discounter.discount(self.cur_time)
```

See [complete code of BSMC here](https://github.com/finlib/finmc/blob/main/finmc/models/localvol.py)

## Examples in other repos

Examples using `MCFixedStep` as base

- [Local Vol using SVI vols](https://github.com/qatwalk/eq/blob/main/src/model/localvol.py)
- [Qablet Intro to Custom Models](https://github.com/qablet-academy/intro/blob/main/notebooks/2_1_custom_mc.ipynb)


Examples using `MCBase`:

- [Rough Bergomi Model](https://github.com/qatwalk/eq/blob/main/src/model/rbergomi.py)