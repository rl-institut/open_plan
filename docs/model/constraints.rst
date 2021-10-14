.. _constraints-label:

Constraints
-----------

.. _constraint_min_re_factor:

Minimal renewable factor constraint
###################################

The minimal renewable factor constraint requires the capacity and dispatch optimization of the open_plan tool to reach at least the minimal renewable factor defined within the constraint. The renewable share of the optimized energy system may also be higher than the minimal renewable factor.

The minimal renewable factor is applied to the minimal renewable factor of the whole, sector-coupled energy system, but not to specific sectors. As such, energy carrier weighting plays a role and may lead to unexpected results. The constraint reads as follows:

.. TODO: express this equation with variables as used with output KPIs

.. math::
        minimal renewable factor <= \frac{\sum renewable generation \cdot weighting factor}{\sum renewable generation \cdot weighting factor + \sum non-renewable generation \cdot weighting factor}

Please be aware that the minimal renewable factor constraint defines bounds for the :ref:`renewable_factor` of the system, ie. taking into account both local generation as well as renewable supply from the energy providers. The constraint explicitly does not aim to reach a certain :ref:`renewable_share_of_local_generation` on-site.

Depending on the energy system, especially when working with assets which are not to be capacity-optimized, it is possible that the minimal renewable factor criterion cannot be met. The simulation terminates in that case. If you are not sure if your energy system can meet the constraint, set all :code:`optimize_Cap` parameters of your optimizable assets to :code:`True`, and then investigate further.

Also, if you are aiming at very high minimal renewable factors, the simulation time can increase drastically. If you do not get a result after an execessive simulation time (e.g. 10 times the simulation without constraints), you should consider terminating the simulation and trying with a lower minimum renewable share.


.. _constraint_minimal_degree_of_autonomy:

Minimal degree of autonomy constraint
######################################

The minimal degree of autonomy constraint requires the capacity and dispatch optimization of the open_plan tool to reach at least the minimal degree of autonomy defined within the constraint. The degree of autonomy of the optimized energy system may also be higher than the minimal degree of autonomy. For more details, refer to the definition of :ref:`degree of autonomy <degree_of_autonomy>`

The minimal degree of autonomy is applied to the whole, sector-coupled energy system, but not to specific sectors. As such, energy carrier weighting plays a role and may lead to unexpected results.

.. TODO clarify what is the intent of this sentence, I would expect an example of an "unexpected results situation"

The constraint reads as follows:

.. math::
        minimal~degree~of~autonomy <= DA = \frac{\sum E_{demand,i} \cdot w_i - \sum E_{consumption,provider,j} \cdot w_j}{\sum E_{demand,i} \cdot w_i}

Depending on the energy system, especially when working with assets which are not subject to the optimization of their capacities, it is possible that the minimal degree of autonomy criterion cannot be met. The simulation terminates in that case. If you are not sure if your energy system can meet the constraint, set all :ref:`optimizecap-label` parameters of your optimizable assets to :code:`True`, and then investigate further.


.. _constraint_maximum_emissions:

Maximum emission constraint
###########################

The maximum emission constraint limits the maximum amount of total emissions per year of the energy system. It allows the capacity and dispatch optimization of the open_plan tool to result into a maximum amount of emissions defined by the maximum emission constraint. The yearly emissions of the optimized energy system may also be lower than the maximum emission constraint.

.. note:: The maximum emissions constraint currently does not take into consideration life cycle emissions, also see :ref:`total_emissions` section for an explanation.

The unit of the constraint is `kgCO2eq/a`. To pick a realistic value for this constraint you can e.g.:

- Firstly, optimize your system without the constraint to get an idea about the scale of the emissions and then, secondly, set the constraint and lower the emissions step by step until you reach an unbound problem (which then represents the non-achievable minimum of emissions for your energy system)
- Check the emissions targets of your region/country and disaggregate the number


.. _constraint_net_zero_energy:

Net zero energy (NZE) constraint
################################

The net zero energy (NZE) constraint requires the capacity and dispatch optimization of the open_plan tool to result into a net zero system, but can also result in a plus energy system.
The degree of NZE of the optimized energy system may be higher than 1, in case of a plus energy system. Please find the definition of net zero energy (NZE) and the KPI here: :ref:`degree_of_nze`.

.. TODO quote the literature references here

Some definitions of NZE systems in literature allow the energy system's demand solely be provided by locally generated renewable energy. In the open_plan tool this is not the case - all locally generated energy is taken into consideration. To enlarge the share of renewables in the energy system you can use the :ref:`constraint_min_re_factor`.

The NZE constraint is applied to the whole, sector-coupled energy system, but not to specific sectors. As such, energy carrier weighting plays a role and may lead to unexpected results. The constraint reads as follows:

.. math::
        \sum_{i} {E_{feedin, provider} (i) \cdot w_i - E_{consumption, provider} (i) \cdot w_i} >= 0

Depending on the energy system, especially when working with assets which are not subject to the optimization of their capacities, it is possible that the NZE criterion cannot be met. The simulation terminates in that case. If you are not sure whether your energy system can meet the constraint, set all :ref:`optimizecap-label` parameters of your optimizable assets to :code:`True`, and then investigate further.
