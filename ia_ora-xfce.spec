Summary:        Ia Ora Mandriva Xfce theme
Name:           ia_ora-xfce
Version:        1.0.1
Release:        %mkrel 1
License:        GPL
Group:          Graphical desktop/Xfce
URL:            http://www.mandrivalinux.com/
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       ia_ora-gnome-gtk2-engine

%description
Mandriva Ia Ora Xfce theme

%prep
%setup -q -n Ia\ Ora

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/%{_datadir}/themes/Ia\ Ora/
mv * %{buildroot}/%{_datadir}/themes/Ia\ Ora/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/themes/*
