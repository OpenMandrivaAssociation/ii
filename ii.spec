%define name ii
%define version 1.3
%define release %mkrel 4

Name:		%name
Version:	%version
Release:	%release
Group:		Networking/Other
URL:		http://www.suckless.org/wiki/programs/ii.html
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root
Source0:	http://www.suckless.org/download/%{name}-%{version}.tar.gz
Summary:	Minimalist FIFO and filesystem-based IRC client
%description
ii is a minimalist FIFO and filesystem-based IRC client. It creates an
irc directory tree with server, channel and nick name directories. In
every directory a FIFO in file and a normal out file is created.

The in file is used to communicate with the servers and the out files
contain the server messages. For every channel and every nick name there
are related in and out files created. This allows IRC communication from
command line and adheres to the Unix philosophy. example

Join a channel as follows: $ echo "/j #wmii" > in and ii creates a
new #wmii (channel) directory with in and out files.

It consists of <= 500 lines of code and is the big brother of sic (simple
irc client).

%prep
%setup -q

%build
make

%install
make PREFIX=$RPM_BUILD_ROOT%{_prefix} install
%{__rm} -Rf $RPM_BUILD_ROOT/usr/share/doc/ii

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE FAQ query.sh
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


