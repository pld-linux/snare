Summary:	A intrusion detection tool for GNOME
Name:		snare
Version:	0.9
Release:	1
License:	GPL
Group:		Applications/System
URL:		http://www.intersectalliance.com/
Source0:	http://www.intersectalliance.com/snare/snare-%{version}.tar.gz
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Graphical User Interface component of the System iNtrusion
Analysis and Reporting Environment (SNARE).

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -d $RPM_BUILD_ROOT%{_applnkdir}/System
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/ximian/Programs/Utilities
install -d $RPM_BUILD_ROOT%{_applnkdir}/System
cp snare-icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp snare-logo.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp snare.desktop $RPM_BUILD_ROOT%{_applnkdir}/System
cp snare.desktop $RPM_BUILD_ROOT%{_datadir}/gnome/ximian/Programs/Utilities
cp Snare.kdelnk $RPM_BUILD_ROOT%{_applnkdir}/System

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

mv $RPM_BUILD_ROOT%{_bindir}/snare $RPM_BUILD_ROOT%{_sbindir}/
ln -s %{_bindir}/consolehelper $RPM_BUILD_ROOT/%{_bindir}/snare

install -d $RPM_BUILD_ROOT/etc/pam.d
cat > $RPM_BUILD_ROOT/etc/pam.d/snare <<EOF
auth       sufficient   /lib/security/pam_rootok.so
auth       required     /lib/security/pam_pwdb.so
session    optional     /lib/security/pam_xauth.so
account    required     /lib/security/pam_permit.so
EOF

install -d $RPM_BUILD_ROOT/etc/security/console.apps
cat > $RPM_BUILD_ROOT/etc/security/console.apps/snare <<EOF
USER=root
FALLBACK=true
PROGRAM=%{_sbindir}/snare
SESSION=true
EOF

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS COPYING
%attr(755,root,root) %{_sbindir}/snare
%{_applnkdir}/System/snare.desktop
%{_datadir}/gnome/ximian/Programs/Utilities/snare.desktop
%{_datadir}/pixmaps/*
%attr(755,root,root) %{_bindir}/snare
/etc/pam.d/snare
/etc/security/console.apps/snare

%clean
rm -r $RPM_BUILD_ROOT
