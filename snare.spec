Summary:	A intrusion detection tool for GNOME
Summary(pl.UTF-8):	Narzędzie do wykrywania intruzów dla GNOME
Name:		snare
Version:	0.9
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.intersectalliance.com/snare/snare-%{version}.tar.gz
URL:		http://www.intersectalliance.com/
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Graphical User Interface component of the System iNtrusion
Analysis and Reporting Environment (SNARE).

%description -l pl.UTF-8
Graficzny interfejs użytkownika dla środowiska analizy i zgłaszania
intruzów SNARE (System iNtrusion Analysis and Reporting Environment).

%prep
%setup -q

echo 'Categories=System;Utility;' >> snare.desktop

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_pixmapsdir},%{_desktopdir}}
install snare-icon.png snare-logo.png $RPM_BUILD_ROOT%{_pixmapsdir}
install snare.desktop $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

mv $RPM_BUILD_ROOT%{_bindir}/snare $RPM_BUILD_ROOT%{_sbindir}
ln -sf %{_bindir}/consolehelper $RPM_BUILD_ROOT%{_bindir}/snare

install -d $RPM_BUILD_ROOT/etc/pam.d
cat > $RPM_BUILD_ROOT/etc/pam.d/snare <<EOF
auth       sufficient   pam_rootok.so
auth       required     pam_unix.so
session    optional     pam_xauth.so
account    required     pam_permit.so
EOF

install -d $RPM_BUILD_ROOT/etc/security/console.apps
cat > $RPM_BUILD_ROOT/etc/security/console.apps/snare <<EOF
USER=root
FALLBACK=true
PROGRAM=%{_sbindir}/snare
SESSION=true
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS COPYING
%attr(755,root,root) %{_sbindir}/snare
%attr(755,root,root) %{_bindir}/snare
%{_desktopdir}/snare.desktop
%{_pixmapsdir}/*
/etc/pam.d/snare
/etc/security/console.apps/snare
