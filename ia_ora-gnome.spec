# SOURCE IS STORED IN SVN (soft/theme/ia_ora-gnome), 
# DO NOT PATCH IT

%define libname %{_lib}ia_ora-gnome

Summary:        Ia Ora Mandriva GNOME theme
Name:           ia_ora-gnome
Version:        1.0.17
Release:        %mkrel 1
License:        GPL
Group: Graphical desktop/GNOME
URL:            http://www.mandrivalinux.com/
BuildRequires:  gtk+2-devel
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: gnome-icon-theme
Requires: ia_ora-gnome-gtk2-engine

%description
Mandriva Ia Ora GNOME theme

%package -n %{libname}
Summary: GTK2 engine for Ia Ora theme
Group: Graphical desktop/GNOME
Provides: ia_ora-gnome-gtk2-engine

%description -n %{libname}
GTK2 engine for Ia Ora theme



 
%prep
%setup -q 

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std


#remove unpackaged files 
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
%doc README 
%{_datadir}/themes/*

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/gtk-2.0/*/engines/*.so


