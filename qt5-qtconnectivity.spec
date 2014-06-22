#
# Conditional build:
%bcond_without	qch	# documentation in QCH format

%define		orgname		qtconnectivity
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 Connectivity libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Connectivity
Name:		qt5-%{orgname}
Version:	5.3.0
Release:	1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.3/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	46e4e8df94b4da4415aa5f5076b8bc45
URL:		http://qt-project.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtbase_ver}
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5DBus-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	bluez-libs-devel
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5DBus >= %{qtbase_ver}
Requires:	Qt5Qml>= %{qtdeclarative_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Connectivity libraries.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera biblioteki Qt5 Connectivity.

%package devel
Summary:	The Qt5 Connectivity - development files
Summary(pl.UTF-8):	Biblioteki Qt5 Connectivity - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5DBus-devel >= %{qtbase_ver}
Requires:	Qt5Qml-devel >= %{qtdeclarative_ver}

%description devel
The Qt5 Connectivity - development files.

%description devel -l pl.UTF-8
Biblioteki Qt5 Connectivity - pliki programistyczne.

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
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Bluetooth.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Bluetooth.so.5
%attr(755,root,root) %{_libdir}/libQt5Nfc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Nfc.so.5
%dir %{qt5dir}/qml/QtBluetooth
%attr(755,root,root) %{qt5dir}/qml/QtBluetooth/libdeclarative_bluetooth.so
%{qt5dir}/qml/QtBluetooth/plugins.qmltypes
%{qt5dir}/qml/QtBluetooth/qmldir
%dir %{qt5dir}/qml/QtNfc
%attr(755,root,root) %{qt5dir}/qml/QtNfc/libdeclarative_nfc.so
%{qt5dir}/qml/QtNfc/plugins.qmltypes
%{qt5dir}/qml/QtNfc/qmldir

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Bluetooth.so
%attr(755,root,root) %{_libdir}/libQt5Nfc.so
%{_libdir}/libQt5Bluetooth.prl
%{_libdir}/libQt5Nfc.prl
%{_includedir}/qt5/QtBluetooth
%{_includedir}/qt5/QtNfc
%{_pkgconfigdir}/Qt5Bluetooth.pc
%{_pkgconfigdir}/Qt5Nfc.pc
%{_libdir}/cmake/Qt5Bluetooth
%{_libdir}/cmake/Qt5Nfc
%{qt5dir}/mkspecs/modules/*.pri

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtbluetooth
%{_docdir}/qt5-doc/qtnfc

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtbluetooth.qch
%{_docdir}/qt5-doc/qtnfc.qch
%endif

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
