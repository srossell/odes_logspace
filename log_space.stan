functions {
    vector odes(real t, vector y, array[] real p) {
        vector[1] dydt;
        dydt[1] = 1/exp(y[1]) - p[1] / (p[2] + exp(y[1]));
        return dydt;
    }
}

data {
    int<lower=1> y_obs_dim0;
    int<lower=1> t_obs_dim0;
    int<lower=1> y0_dim0;
    array[y_obs_dim0] real y_obs;
    array[t_obs_dim0] real t_obs;
    vector[y0_dim0] y0;
}

parameters {
    array[2] real<lower=0> p;
    vector<lower=0>[y0_dim0] sigma;
}

transformed parameters {
    array[t_obs_dim0] vector[y0_dim0] y_sim;
    y_sim = ode_bdf(odes, y0, 0, t_obs, p);
}

model {
    p[1] ~ gamma(1.30, 3.03);  // Larger than 1 is very unlikely
    p[2] ~ gamma(2, 0.5);  // Larger than 10 is very unlikely
    sigma ~ gamma(2, 0.5); // I don't know how to choose this one!
    for (i in 1:y_obs_dim0) {
        y_obs[i] ~ normal(y_sim[i], sigma);
    }
}
