%define		kdeframever	5.91
%define		qtver		5.15.2
%define		kfname		kservice

Summary:	Plugin framework for desktop services
Name:		kf5-%{kfname}
Version:	5.91.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	b45f86503ff166a69a7cd2fc2f3fdca2
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	bison >= 3.0
BuildRequires:	cmake >= 3.16
BuildRequires:	flex
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5Xml >= %{qtver}
Requires:	kf5-dirs
Requires:	kf5-kconfig >= %{version}
Requires:	kf5-kcoreaddons >= %{version}
Requires:	kf5-kdbusaddons >= %{version}
Requires:	kf5-ki18n >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KService provides a plugin framework for handling desktop services.
Services can be applications or libraries. They can be bound to MIME
types or handled by application specific code.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cmake >= 3.16
Requires:	kf5-kconfig-devel >= %{version}
Requires:	kf5-kcoreaddons-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
/etc/xdg/menus/applications.menu
%attr(755,root,root) %{_bindir}/kbuildsycoca5
%ghost %{_libdir}/libKF5Service.so.5
%attr(755,root,root) %{_libdir}/libKF5Service.so.*.*
%{_datadir}/kservicetypes5/application.desktop
%{_datadir}/kservicetypes5/kplugininfo.desktop
%{_mandir}/man8/desktoptojson.8*
%{_mandir}/man8/kbuildsycoca5.8*
%lang(ca) %{_mandir}/ca/man8/desktoptojson.8*
%lang(ca) %{_mandir}/ca/man8/kbuildsycoca5.8*
%lang(de) %{_mandir}/de/man8/desktoptojson.8*
%lang(de) %{_mandir}/de/man8/kbuildsycoca5.8*
%lang(es) %{_mandir}/es/man8/desktoptojson.8*
%lang(es) %{_mandir}/es/man8/kbuildsycoca5.8*
%lang(it) %{_mandir}/it/man8/desktoptojson.8*
%lang(it) %{_mandir}/it/man8/kbuildsycoca5.8*
%lang(nl) %{_mandir}/nl/man8/desktoptojson.8*
%lang(nl) %{_mandir}/nl/man8/kbuildsycoca5.8*
%lang(pt) %{_mandir}/pt/man8/desktoptojson.8*
%lang(pt) %{_mandir}/pt/man8/kbuildsycoca5.8*
%lang(pt_BR) %{_mandir}/pt_BR/man8/desktoptojson.8*
%lang(pt_BR) %{_mandir}/pt_BR/man8/kbuildsycoca5.8*
%lang(sv) %{_mandir}/sv/man8/desktoptojson.8*
%lang(sv) %{_mandir}/sv/man8/kbuildsycoca5.8*
%lang(uk) %{_mandir}/uk/man8/desktoptojson.8*
%lang(uk) %{_mandir}/uk/man8/kbuildsycoca5.8*
%lang(id) %{_mandir}/id/man8/desktoptojson.8*
%{_datadir}/qlogging-categories5/kservice.categories
%lang(fr) %{_mandir}/fr/man8/kbuildsycoca5.8*
%{_datadir}/qlogging-categories5/kservice.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KService
%{_libdir}/cmake/KF5Service
%{_libdir}/libKF5Service.so
%{qt5dir}/mkspecs/modules/qt_KService.pri
