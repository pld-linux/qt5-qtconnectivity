# TODO:
# - cleanup

%define		orgname		qtconnectivity
Summary:	The Qt5 Connectivity
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	bee0760e1bf6e89d8fdceb6ea6cd50a1
URL:		http://qt-project.org/
BuildRequires:	bluez-libs-devel
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	qt5-qtdeclarative-devel = %{version}
BuildRequires:	qt5-qttools-devel = %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_noautostrip	'.*_debug\\.so*'

%define		specflags	-fno-strict-aliasing
%define		_qtdir		%{_libdir}/qt5

%description
The Qt5 Connectivity libraries.

%package devel
Summary:	The Qt5 Connectivity - development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The Qt5 Connectivity - development files.

%package doc
Summary:	The Qt5 Connectivity - docs
Group:		Documentation

%description doc
The Qt5 Connectivity - documentation.

%package examples
Summary:	The Qt5 Connectivity examples
Group:		X11/Development/Libraries

%description examples
The Qt5 Connectivity - examples.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post		-p /sbin/ldconfig
%postun		-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libQt5Bluetooth.so.?
%attr(755,root,root) %{_libdir}/libQt5Bluetooth.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Nfc.so.?
%attr(755,root,root) %{_libdir}/libQt5Nfc.so.*.*
%{_qtdir}/qml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Bluetooth.so
%attr(755,root,root) %{_libdir}/libQt5Nfc.so
%{_libdir}/libQt5Bluetooth.la
%{_libdir}/libQt5Nfc.la
%{_libdir}/libQt5Bluetooth.prl
%{_libdir}/libQt5Nfc.prl
%{_libdir}/cmake/Qt5Bluetooth
%{_libdir}/cmake/Qt5Nfc
%{_includedir}/qt5/QtBluetooth
%{_includedir}/qt5/QtNfc
%{_pkgconfigdir}/*.pc
%{_qtdir}/mkspecs

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc
