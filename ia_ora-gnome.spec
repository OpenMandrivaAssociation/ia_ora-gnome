# SOURCE IS STORED IN SVN (soft/theme/ia_ora-gnome), 
# DO NOT PATCH IT
%define _disable_lto 1

%define libname %{_lib}ia_ora-gnome

Summary:	Ia Ora Mandriva GNOME theme
Name:		ia_ora-gnome
Version:	1.0.24
Release:	17
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		https://www.mandrivalinux.com/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	gnome-icon-theme
Requires:	ia_ora-gnome-gtk2-engine

%description
Mandriva Ia Ora GNOME theme

%package -n %{libname}
Summary:	GTK2 engine for Ia Ora theme
Group:		System/Libraries
Provides:	ia_ora-gnome-gtk2-engine

%description -n %{libname}
GTK2 engine for Ia Ora theme
 
%prep
%setup -q 

%build
%configure2_5x

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/themes/Ia\ Ora\ Free %{buildroot}%{_datadir}/themes/Ia\ Ora\ One

%pre
if [ -d %{_datadir}/themes/Ia\ Ora\ Free -a ! -L %{_datadir}/themes/Ia\ Ora\ Free ]; then 
 /bin/rm -rf %{_datadir}/themes/Ia\ Ora\ Free/* || /bin/true
fi

if [ -d %{_datadir}/themes/Ia\ Ora\ One -a ! -L %{_datadir}/themes/Ia\ Ora\ One ]; then 
 /bin/rm -rf %{_datadir}/themes/Ia\ Ora\ One/* || bin/true
fi

%posttrans
# create compatibility symlinks
ln -f -s ../Ia\ Ora\ Smooth/metacity-1 %{_datadir}/themes/Ia\ Ora\ One/metacity-1
ln -f -s ../Ia\ Ora\ Smooth/gtk-2.0 %{_datadir}/themes/Ia\ Ora\ One/gtk-2.0
ln -f -s ../Ia\ Ora\ Arctic/metacity-1 %{_datadir}/themes/Ia\ Ora\ Free/metacity-1
ln -f -s ../Ia\ Ora\ Arctic/gtk-2.0 %{_datadir}/themes/Ia\ Ora\ Free/gtk-2.0

%preun 
if [ "$1" = "0" ]; then
 /bin/rm -f %{_datadir}/themes/Ia\ Ora\ Free/* %{_datadir}/themes/Ia\ Ora\ One/*   || /bin/true
fi


%files 
%doc README 
%{_datadir}/themes/*

%files -n %{libname}
%{_libdir}/gtk-2.0/*/engines/*.so

