#
# Conditional build:
%bcond_without	doc	# Documentation
%bcond_without	qm	# QM translations

%define		orgname		qtconnectivity
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 Connectivity libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Connectivity
Name:		qt5-%{orgname}
Version:	5.12.2
Release:	1
License:	LGPL v2.1 with Digia Qt LGPL Exception v1.1 or GPL v3.0
Group:		Libraries
Source0:	http://download.qt.io/official_releases/qt/5.12/%{version}/submodules/%{orgname}-everywhere-src-%{version}.tar.xz
# Source0-md5:	c4acfbb83f74a7fbbcadd378055d7cef
Source1:	http://download.qt.io/official_releases/qt/5.12/%{version}/submodules/qttranslations-everywhere-src-%{version}.tar.xz
# Source1-md5:	298e993499be31ab95162b61456a4b25
URL:		http://www.qt.io/
BuildRequires:	Qt5Concurrent-devel >= %{qtbase_ver}
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5DBus-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	bluez-libs-devel
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
%{?with_qm:BuildRequires:	qt5-linguist >= %{qttools_ver}}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Connectivity libraries: Qt5Bluetooth and
QtNfc.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera biblioteki Qt5 Connectivity: Qt5Bluetooth i Qt5Nfc.

%package common
Summary:	Common files used by all Qt5 Connectivity components
Summary(pl.UTF-8):	Wspólne pliki wykorzystywane przez wszystkie komponenty Qt5 Connectivity
Group:		Libraries

%description common
Common files used by all Qt5 Connectivity components.

%description common -l pl.UTF-8
Wspólne pliki wykorzystywane przez wszystkie komponenty Qt5
Connectivity.

%package -n Qt5Bluetooth
Summary:	Qt5 Bluetooth library
Summary(pl.UTF-8):	Biblioteka Qt5 Bluetooth
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5DBus >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Obsoletes:	qt5-qtconnectivity

%description -n Qt5Bluetooth
Qt5 Bluetooth library provides classes that enable basic Bluetooth
operations like scanning for devices and connecting them.

%description -n Qt5Bluetooth -l pl.UTF-8
Biblioteka Qt5 Bluetooth dostarcza klasy umożliwiające podstawowe
operacje Bluetooth, takie jak wyszukiwanie urządzeń i łączenie z nimi.

%package -n Qt5Bluetooth-devel
Summary:	The Qt5 Bluetooth - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Bluetooth - pliki programistyczne
Group:		Development/Libraries
Requires:	Qt5Bluetooth = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5DBus-devel >= %{qtbase_ver}
Requires:	Qt5Qml-devel >= %{qtdeclarative_ver}
Obsoletes:	qt5-qtconnectivity-devel

%description -n Qt5Bluetooth-devel
The Qt5 Bluetooth - development files.

%description -n Qt5Bluetooth-devel -l pl.UTF-8
Biblioteka Qt5 Bluetooth - pliki programistyczne.

%package -n Qt5Nfc
Summary:	Qt5 Nfc library
Summary(pl.UTF-8):	Biblioteka Qt5 Nfc
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5DBus >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Obsoletes:	qt5-qtconnectivity

%description -n Qt5Nfc
Qt5 Nfc library provides classes to access NFC Forum Tags.

%description -n Qt5Nfc -l pl.UTF-8
Biblioteka Qt5 Nfc dostarcza klasy służace do dostępu do urządzeń NFC
Forum.

%package -n Qt5Nfc-devel
Summary:	The Qt5 Nfc - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Nfc - pliki programistyczne
Group:		Development/Libraries
Requires:	Qt5Nfc = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5DBus-devel >= %{qtbase_ver}
Requires:	Qt5Qml-devel >= %{qtdeclarative_ver}
Obsoletes:	qt5-qtconnectivity-devel

%description -n Qt5Nfc-devel
The Qt5 Nfc - development files.

%description -n Qt5Nfc-devel -l pl.UTF-8
Biblioteka Qt5 Nfc - pliki programistyczne.

%package doc
Summary:	Qt5 Connectivity documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Connectivity w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Connectivity documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Connectivity w formacie HTML.

%package doc-qch
Summary:	Qt5 Connectivity documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Connectivity w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-qch
Qt5 Connectivity documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Connectivity w formacie QCH.

%package examples
Summary:	Qt5 Connectivity examples
Summary(pl.UTF-8):	Przykłady do bibliotek Qt5 Connectivity
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 Connectivity examples.

%description examples -l pl.UTF-8
Przykłady do bibliotek Qt5 Connectivity.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version} %{?with_qm:-a1}

%build
qmake-qt5
%{__make}
%{?with_doc:%{__make} docs}

%if %{with qm}
cd qttranslations-everywhere-src-%{version}
qmake-qt5
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

%if %{with qm}
%{__make} -C qttranslations-everywhere-src-%{version} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# keep only qtconnectivity
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/{assistant,designer,linguist,qt,qtbase,qtdeclarative,qtlocation,qtmultimedia,qtquickcontrols,qtquickcontrols2,qtserialport,qtscript,qtwebengine,qtwebsockets,qtxmlpatterns}_*.qm
%endif

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.??
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# Prepare some files list
ifecho() {
	r="$RPM_BUILD_ROOT$2"
	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or directory!"
		return 1
	fi
}
ifecho_tree() {
	ifecho $1 $2
	for f in `find $RPM_BUILD_ROOT$2 -printf "%%P "`; do
		ifecho $1 $2/$f
	done
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho_tree examples %{_examplesdir}/qt5/bluetooth
ifecho_tree examples %{_examplesdir}/qt5/nfc

# find_lang --with-qm supports only PLD qt3/qt4 specific %{_datadir}/locale/*/LC_MESSAGES layout
find_qt5_qm()
{
	name="$1"
	find $RPM_BUILD_ROOT%{_datadir}/qt5/translations -name "${name}_*.qm" | \
		sed -e "s:^$RPM_BUILD_ROOT::" \
		    -e 's:\(.*/'$name'_\)\([a-z][a-z][a-z]\?\)\(_[A-Z][A-Z]\)\?\(\.qm\)$:%lang(\2\3) \1\2\3\4:'
}

echo '%defattr(644,root,root,755)' > qtconnectivity.lang
%if %{with qm}
find_qt5_qm qtconnectivity >> qtconnectivity.lang
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5Bluetooth -p /sbin/ldconfig
%postun	-n Qt5Bluetooth -p /sbin/ldconfig

%post	-n Qt5Nfc -p /sbin/ldconfig
%postun	-n Qt5Nfc -p /sbin/ldconfig

%files common -f qtconnectivity.lang
%defattr(644,root,root,755)
%doc LICENSE.GPL3-EXCEPT dist/changes-*

%files -n Qt5Bluetooth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Bluetooth.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Bluetooth.so.5
%attr(755,root,root) %{qt5dir}/bin/sdpscanner
%dir %{qt5dir}/qml/QtBluetooth
%attr(755,root,root) %{qt5dir}/qml/QtBluetooth/libdeclarative_bluetooth.so
%{qt5dir}/qml/QtBluetooth/plugins.qmltypes
%{qt5dir}/qml/QtBluetooth/qmldir

%files -n Qt5Bluetooth-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Bluetooth.so
%{_libdir}/libQt5Bluetooth.prl
%{_includedir}/qt5/QtBluetooth
%{_pkgconfigdir}/Qt5Bluetooth.pc
%{_libdir}/cmake/Qt5Bluetooth
%{qt5dir}/mkspecs/modules/qt_lib_bluetooth.pri
%{qt5dir}/mkspecs/modules/qt_lib_bluetooth_private.pri

%files -n Qt5Nfc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Nfc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Nfc.so.5
%dir %{qt5dir}/qml/QtNfc
%attr(755,root,root) %{qt5dir}/qml/QtNfc/libdeclarative_nfc.so
%{qt5dir}/qml/QtNfc/plugins.qmltypes
%{qt5dir}/qml/QtNfc/qmldir

%files -n Qt5Nfc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Nfc.so
%{_libdir}/libQt5Nfc.prl
%{_includedir}/qt5/QtNfc
%{_pkgconfigdir}/Qt5Nfc.pc
%{_libdir}/cmake/Qt5Nfc
%{qt5dir}/mkspecs/modules/qt_lib_nfc.pri
%{qt5dir}/mkspecs/modules/qt_lib_nfc_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtbluetooth
%{_docdir}/qt5-doc/qtnfc

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtbluetooth.qch
%{_docdir}/qt5-doc/qtnfc.qch
%endif

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
