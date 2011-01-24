#
# TODO: icon
#
Summary:	Ultima V game engine clone with enhanced features
Summary(pl.UTF-8):	Gra oparata o ulepszony silnik Ultimy V
Name:		nazghul
Version:	0.7.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/nazghul/%{name}-%{version}.tar.gz
# Source0-md5:	78b46488f1b8fee62a4b839d2ff6b167
Patch0:		%{name}-default_cfg.patch
URL:		http://myweb.cableone.net/gmcnutt/nazghul.html
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nazghul is an old-school RPG based on Ultima V game engine.

%description -l pl.UTF-8
Nazghul jest grą RPG starej szkoły, opartą o silnik Ultimy V.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove useless doc stuff
%{__rm} -r doc/{CVS,engine_extension_and_design,null.gif,world_building}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
