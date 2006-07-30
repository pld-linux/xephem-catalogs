Summary:	Additional XEphen catalogs
Summary(pl):	Dodatkowe katalogi do XEphema
Name:		xephem-catalogs
Version:	1.0
Release:	1
License:	distributable
Group:		X11/Applications/Science
Source0:	http://www.yvonnet.org/xephem/sky2000.edb.gz
# Source0-md5:	c3f5289fe2a4a2935581830c13138e90
Source1:	http://www.yvonnet.org/xephem/hipparcos.edb.gz
# Source1-md5:	274311da49f94296d4bea4014819e438
Source2:	http://www.yvonnet.org/xephem/ngc.edb.gz
# Source2-md5:	c05d14ce5c98bde693e4da019464ee31
Source3:	http://hexadecimal.uoregon.edu/~stevev/xephemcatalogs/tycho2.xe2
# Source3-md5:	ba25e8e580269bbcbd4a1c84bde10355
URL:		http://cdsweb.u-strasbg.fr/cats/cats.html
Requires:	xephem >= 3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional XEphem catalogs generated from data available at
http://cdsweb.u-strasbg.fr/cats/cats.html

- Hipparcos Input Catalogue, Version 2 (Turon+ 1993)	(I/196)
- NGC 2000.0 (Sky Publishing, ed. Sinnott 1988)		(VII/118)
- SKY2000 Catalog, Version 3 (Myers+ 2000)		(V/105)

To use this catalogs you must enable them in Data/Files submenu in
main XEphem window.

%description -l pl
Dodatkowe katalogi do XEphema wygenerowane na podstawie danych
dostêpnych pod adresem: http://cdsweb.u-strasbg.fr/cats/cats.html

- Hipparcos Input Catalogue, Version 2 (Turon+ 1993)	(I/196)
- NGC 2000.0 (Sky Publishing, ed. Sinnott 1988)		(VII/118)
- SKY2000 Catalog, Version 3 (Myers+ 2000)		(V/105)

Aby u¿yæ tych katalogów musisz w³±czyæ je w podmenu Data/Files
g³ównego okna XEphema.

%package tycho2
Summary:	Hipparcos/Tycho2 field stars catalog for XEphem
Summary(pl):	Hipparcos/Tycho2 katalog dla Xephema
Group:		X11/Applications/Science

%description tycho2
Hipparcos/Tycho2 catalog generated from from data available at
http://cdsweb.u-strasbg.fr/cats/cats.html

- The Hipparcos and Tycho Catalogues (ESA 1997)		(I/239)
- The Tycho-2 Catalogue (Hog+ 2000)			(I/259)

To use this catalog you must enable it in Data/Field Stars submenu
in main XEphem window.

%description tycho2 -l pl
Katalog Hipparcos/Tycho2 wygenerowany na podstawie danych dostêpnych
pod adresem: http://cdsweb.u-strasbg.fr/cats/cats.html

- The Hipparcos and Tycho Catalogues (ESA 1997)		(I/239)
- The Tycho-2 Catalogue (Hog+ 2000)			(I/259)

Aby u¿yæ tego katalogu musisz go w³±czyæ w podmenu Data/Field Stars
g³ównego okna XEphema.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xephem/catalogs

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/xephem/catalogs
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xephem/catalogs
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xephem/catalogs
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/xephem/catalogs/hiptyc2.xe2

gunzip $RPM_BUILD_ROOT%{_datadir}/xephem/catalogs/*.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xephem/catalogs/ngc.edb
%{_datadir}/xephem/catalogs/hipparcos.edb
%{_datadir}/xephem/catalogs/sky2000.edb

%files tycho2
%defattr(644,root,root,755)
%{_datadir}/xephem/catalogs/hiptyc2.xe2
