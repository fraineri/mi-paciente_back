from dependency_injector import containers, providers


class CoreServicesContainer(containers.DeclarativeContainer):
    settings = providers.DependenciesContainer()
    persistance = providers.DependenciesContainer()
