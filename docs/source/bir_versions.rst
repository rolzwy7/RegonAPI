BIR Versions
============

To this date there are two version of BIR service.

- BIR v1.0 (2015)
- BIR v1.1 (2019)


Main differences
^^^^^^^^^^^^^^^^

**WSDL and Service URL are different between versions**

- BIR v1

Test - Service URL:
https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc

Test - WSDL:
https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl.xsd

Production - Service URL:
https://wyszukiwarkaregon.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc

Production - WSDL:
https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl.xsd

- BIR v1.1

Test - Service URL:
https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc

Test - WSDL:
https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-test.wsdl

Production - Service URL:
https://wyszukiwarkaregon.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc

Production - WSDL:
https://wyszukiwarkaregon.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-prod.wsdl

**Names of available reports are different**

=========================================== ==============================================
                **BIR 1.0**                                 **BIR 1.1**
=========================================== ==============================================
PublDaneRaportFizycznaOsoba                 BIR11OsFizycznaDaneOgolne
PublDaneRaportDzialalnoscFizycznejCeidg     BIR11OsFizycznaDzialalnoscCeidg
PublDaneRaportDzialalnoscFizycznejRolnicza  BIR11OsFizycznaDzialalnoscRolnicza
PublDaneRaportDzialalnoscFizycznejPozostala BIR11OsFizycznaDzialalnoscPozostala
PublDaneRaportDzialalnoscFizycznejWKrupgn   BIR11OsFizycznaDzialalnoscSkreslonaDo2014
PublDaneRaportDzialalnosciFizycznej         BIR11OsFizycznaPkd
PublDaneRaportLokalneFizycznej              BIR11OsFizycznaListaJednLokaln
PublDaneRaportLokalnaFizycznej              BIR11JednLokalnaOsFizycznej
PublDaneRaportDzialalnosciLokalnejFizycznej BIR11JednLokalnaOsFizycznejPkd
PublDaneRaportPrawna                        BIR11OsPrawna
PublDaneRaportDzialalnosciPrawnej           BIR11OsPrawnaPkd
PublDaneRaportLokalnePrawnej                BIR11OsPrawnaListaJednLokaln
PublDaneRaportLokalnaPrawnej                BIR11JednLokalnaOsPrawnej
PublDaneRaportDzialalnosciLokalnejPrawnej   BIR11JednLokalnaOsPrawnejPkd
PublDaneRaportWspolnicyPrawnej              BIR11OsPrawnaSpCywilnaWspolnic
PublDaneRaportTypJednostki                  BIR11TypPodmiotu
=========================================== ==============================================

Other differences are listed in official documentation of BIR 1.1

- `BIR Version 1 Documentation <https://api.stat.gov.pl/Content/files/regon/regon_-_instrukcja_techniczna_bir1_dla_podmiotow_komercyjnych_v019.zip>`_

- `BIR Version 1.1 Documentation <https://api.stat.gov.pl/Content/files/regon/GUS-Regon-UslugaBIR11-dokumentacja_v1.02.zip>`_
