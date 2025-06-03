.. image:: https://github.com/Lbalkenhol/candl/raw/main/docs/logos/candl_wordmark&symbol_col_RGB.png
    :width: 800

.. |docsshield| image:: https://img.shields.io/readthedocs/candl
   :target: http://candl.readthedocs.io

.. |arxivshield| image:: https://img.shields.io/badge/arXiv-2401.13433-b31b1b.svg
   :target: https://arxiv.org/abs/2401.13433

Data for ``candl``
===============================================================

:Authors: L\. Balkenhol, C\. Trendafilova, K\. Benabed, S\. Galli

:Paper: |arxivshield|

:Source: `<https://github.com/Lbalkenhol/candl>`__

:Documentation: |docsshield|

Data for `candl <https://github.com/Lbalkenhol/candl>`__  - the differentiable likelihood for CMB analysis.


Installation
------------------------

To install the candl data library, simply navigate to where you would like to store the data and then run::

    git clone https://github.com/Lbalkenhol/candl_data.git
    cd candl_data
    pip install .

This will download the relevant data files. The installation gives you access to handy short cuts, so you don't need to point to the data set ``.yaml`` files directly. To see what's available, run the following python code::

    import candl_data
    candl_data.print_all_shortcuts()


Available Data
------------------------

Please consult the `documentation <https://candl.readthedocs.io/en/stable/data/data_overview.html>`__ for a full description of the available data sets and their usage.
The following table provides a summary.

.. list-table::
   :header-rows: 1
   :widths: 20 25 25

   * - Name
     - Shortcut
     - Papers

   * - SPT-3G 2018 TT/TE/EE
     - ``candl_data.SPT3G_2018_TTTEEE``
     - `Balkenhol et al. 2023 <https://arxiv.org/abs/2212.05642>`__

   * - SPT-3G 2018 :math:`\phi\phi`
     - ``candl_data.SPT3G_2018_Lens``
     - `Pan et al. 2023 <https://arxiv.org/abs/2308.11608>`__

   * - ACT DR6 TT/TE/EE
     - ``candl_data.ACT_DR6_TTTEEE``
     - | `Naess et al. 2025 <https://arxiv.org/abs/2503.14451>`__
       
       `Louis et al. 2025 <https://arxiv.org/abs/2503.14452>`__
       
       `Calabrese et al. 2025 <https://arxiv.org/abs/2503.14454>`__

   * - ACT DR6 :math:`\phi\phi`
     - ``candl_data.ACT_DR6_Lens``
     - | `Madhavacheril et al. 2023 <https://arxiv.org/abs/2304.05203>`__
       
       `Qu et al. 2023 <https://arxiv.org/abs/2304.05202>`__

   * - Planck likelihoods
     - See ``clipy`` (`here <https://github.com/benabed/clipy>`__)
     - `Planck 2018 V <https://arxiv.org/abs/1907.12875>`__

   * - ACT DR4 TT/TE/EE
     - ``candl_data.ACT_DR4_TTTEEE``
     - | `Aiola et al. 2020 <https://arxiv.org/abs/2007.07288>`__
       
       `Choi et al. 2020 <https://arxiv.org/abs/2007.07289>`__


===================

.. |cnrs| image:: https://github.com/Lbalkenhol/candl/raw/main/logos/cnrs_logo.jpeg
   :alt: CNRS
   :height: 100px
   :width: 100px

.. |erc| image:: https://github.com/Lbalkenhol/candl/raw/main/logos/erc_logo.jpeg
   :alt: ERC
   :height: 100px
   :width: 100px

.. |NEUCosmoS| image:: https://github.com/Lbalkenhol/candl/raw/main/logos/neucosmos_logo.png
   :alt: NEUCosmoS
   :height: 100px
   :width: 159px

.. |IAP| image:: https://github.com/Lbalkenhol/candl/raw/main/logos/IAP_logo.jpeg
   :alt: IAP
   :height: 100px
   :width: 104px

.. |Sorbonne| image:: https://github.com/Lbalkenhol/candl/raw/main/logos/sorbonne_logo.jpeg
   :alt: Sorbonne
   :height: 100px
   :width: 248px

|cnrs| |erc| |NEUCosmoS| |IAP| |Sorbonne|
