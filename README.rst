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

.. |arxiv_2212.05642| image:: https://img.shields.io/badge/arXiv-2212.05642-b31b1b.svg
   :target: https://arxiv.org/abs/2212.05642

.. |arxiv_2308.11608| image:: https://img.shields.io/badge/arXiv-2308.11608-b31b1b.svg
   :target: https://arxiv.org/abs/2308.11608

.. |arxiv_2503.14451| image:: https://img.shields.io/badge/arXiv-2503.14451-b31b1b.svg
   :target: https://arxiv.org/abs/2503.14451

.. |arxiv_2503.14452| image:: https://img.shields.io/badge/arXiv-2503.14452-b31b1b.svg
   :target: https://arxiv.org/abs/2503.14452

.. |arxiv_2503.14454| image:: https://img.shields.io/badge/arXiv-2503.14454-b31b1b.svg
   :target: https://arxiv.org/abs/2503.14454

.. |arxiv_2007.07288| image:: https://img.shields.io/badge/arXiv-2007.07288-b31b1b.svg
   :target: https://arxiv.org/abs/2007.07288

.. |arxiv_2007.07289| image:: https://img.shields.io/badge/arXiv-2007.07289-b31b1b.svg
   :target: https://arxiv.org/abs/2007.07289

.. |arxiv_2304.05203| image:: https://img.shields.io/badge/arXiv-2304.05203-b31b1b.svg
   :target: https://arxiv.org/abs/2304.05203

.. |arxiv_2304.05202| image:: https://img.shields.io/badge/arXiv-2304.05202-b31b1b.svg
   :target: https://arxiv.org/abs/2304.05202

.. |arxiv_1907.12875| image:: https://img.shields.io/badge/arXiv-1907.12875-b31b1b.svg
   :target: https://arxiv.org/abs/1907.12875


.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Name
     - Shortcut
     - Papers

   * - SPT-3G 2018 TT/TE/EE
     - ``candl_data.SPT3G_2018_TTTEEE``
     - `Balkenhol et al. 2023 <https://arxiv.org/abs/2212.05642>`__ |arxiv_2212.05642|

   * - SPT-3G 2018 Lensing
     - ``candl_data.SPT3G_2018_Lens``
     - `Pan et al. 2023 <https://arxiv.org/abs/2308.11608>`__ |arxiv_2308.11608|

   * - ACT DR6 TT/TE/EE
     - ``candl_data.ACT_DR6_TTTEEE``
     - `Naess et al. 2025 <https://arxiv.org/abs/2503.14451>`__ |arxiv_2503.14451|,  
       `Louis et al. 2025 <https://arxiv.org/abs/2503.14452>`__ |arxiv_2503.14452|,  
       `Calabrese et al. 2025 <https://arxiv.org/abs/2503.14454>`__ |arxiv_2503.14454|

   * - ACT DR6 Lensing
     - ``candl_data.ACT_DR6_Lens``
     - `Madhavacheril et al. 2023 <https://arxiv.org/abs/2304.05203>`__ |arxiv_2304.05203|,  
       `Qu et al. 2023 <https://arxiv.org/abs/2304.05202>`__ |arxiv_2304.05202|

   * - Planck likelihoods
     - See ``clipy`` <https://github.com/benabed/clipy>`__ 
     - `Planck 2018 cosmological parameters <https://arxiv.org/abs/1907.12875>`__ |arxiv_1907.12875|

   * - ACT DR4 TT/TE/EE
     - ``candl_data.ACT_DR4_TTTEEE``
     - `Aiola et al. 2020 <https://arxiv.org/abs/2007.07288>`__ |arxiv_2007.07288|,  
       `Choi et al. 2020 <https://arxiv.org/abs/2007.07289>`__ |arxiv_2007.07289|
